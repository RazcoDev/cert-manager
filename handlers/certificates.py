from jumpssh import SSHSession
from interfaces.certificate import CertificateFile
from datetime import datetime
from utils.date import convert_pem_date_to_datetime


def get_host_certs_list(host_session: SSHSession, certs_path: str, ) -> list:
    try:
        certs_list = []
        host_certs_output_list = (host_session.get_cmd_output(f'find {certs_path} -name "*.cert.pem"')).split('\r\n')
        for cert_path in host_certs_output_list:
            certs_list.append(CertificateFile(cert_path,host_session.username, host_session.host))
        return certs_list
    except Exception as e:
        print("Could not get hosts certificates list")
        raise e


def get_cert_expiration_date(host_session: SSHSession, certificate_file: CertificateFile, ) -> datetime:
    try:
        date_from_host = host_session.get_cmd_output(
            f'openssl x509 -enddate -noout -in "{certificate_file.file_path}" |cut -d= -f 2)')
        return convert_pem_date_to_datetime(date_from_host)
    except Exception as e:
        print("Could not get certificate expiration date")
        raise e


def create_new_cert_on_host(host_session: SSHSession, certificate_file: CertificateFile, ca_cert: str, ca_key: str):
    try:
        ca_cert_file_path = '/tmp/ca.cert.pem'

        ca_key_file_path = '/tmp/ca.key.pem'
        host_session.run_cmd(f'echo "{ca_cert}" > {ca_cert_file_path}; echo "{ca_key}" > {ca_key_file_path} ')
        host_session.run_cmd(f'openssl x509 -in {ca_cert_file_path} -out {certificate_file.file_path}.new -days 365  \
                                -signkey {ca_key_file_path} -sha256')

    except Exception as e:
        print("Could not create new certificate file")
        raise e
