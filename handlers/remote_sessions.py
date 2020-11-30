from jumpssh import SSHSession
from configs.envs import ID_RSA_PATH


def get_tunnel_session(host_address: str, host_user: str, host_key_path: str = ID_RSA_PATH) -> SSHSession:
    try:
        return SSHSession(host_address, host_user, private_key_file=host_key_path).open()
    except Exception as e:
        print("Could not connect to tunnel host")
        raise e


def get_remote_session(tunnel_session: SSHSession, host_address: str, host_user: str,
                       host_key_path: str = ID_RSA_PATH) -> SSHSession:
    try:
        return tunnel_session.get_remote_session(host_address, host_user, private_key_file=host_key_path)
    except Exception as e:
        print("Could not connect to remote host")
        raise e

