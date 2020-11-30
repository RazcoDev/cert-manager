from jumpssh import SSHSession
from handlers.certificates import create_new_cert_on_host
from handlers.remote_sessions import get_remote_session, get_tunnel_session
from interfaces.certificate import CertificateFile
from configs.envs import HOST_USER


def create_expired_certs(expired_certs_list: list, tunnel_host: str, ca_cert: str, ca_key: str):
    try:
        tunnel_session = get_tunnel_session(tunnel_host, HOST_USER)
        for expired_cert in expired_certs_list:
            _create_expired_cert_on_host(expired_cert, tunnel_session, ca_cert, ca_key)
    except Exception as e:
        raise e


def _create_expired_cert_on_host(certFile: CertificateFile, tunnel_host: SSHSession, ca_cert: str, ca_key: str):
    try:
        host_session = get_remote_session(tunnel_host, certFile.host, certFile.host_user)
        create_new_cert_on_host(host_session, certFile, ca_cert, ca_key)
    except Exception as e:
        raise e
