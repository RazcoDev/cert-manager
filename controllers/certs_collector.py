from jumpssh import SSHSession
from handlers.certificates import get_cert_expiration_date, get_host_certs_list
from handlers.remote_sessions import get_remote_session, get_tunnel_session
from utils.date import is_expiration_date_due
from configs.envs import HOST_USER


def get_expired_certs_list_from_config(config_yaml_dict: dict) -> list:
    try:
        total_expired_certs_list = []
        tunnel_session = get_tunnel_session(config_yaml_dict['bastion'], HOST_USER)
        for host in config_yaml_dict['hosts']:
            host_session = get_remote_session(tunnel_session, host['host'], host['user'])
            host_expired_certs_list = _get_expired_certs_list_from_host(host_session, host['certs_dir'])
            total_expired_certs_list.append(host_expired_certs_list)
        return total_expired_certs_list
    except Exception as e:
        raise e


def _get_expired_certs_list_from_host(host_session: SSHSession, certs_path: str) -> list:
    try:
        certs_list = get_host_certs_list(host_session, certs_path)
        expired_certs_list = []
        for cert in certs_list:
            cert_expiration_date = get_cert_expiration_date(host_session, cert)
            if is_expiration_date_due(cert_expiration_date):
                cert.set_expiration_date(cert_expiration_date)
                expired_certs_list.append(cert)
        return expired_certs_list
    except Exception as e:
        raise e
