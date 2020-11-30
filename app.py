from controllers.certs_collector import get_expired_certs_list_from_config
from controllers.certs_creator import create_expired_certs
from utils.yaml import get_dict_from_yaml_file
from utils.files import get_cert_file_content
from configs.envs import YAML_FILE

if __name__ == '__main__':
    try:
        config_yaml_dict = get_dict_from_yaml_file(YAML_FILE)
        expired_certs_list = get_expired_certs_list_from_config(config_yaml_dict)
        if len(expired_certs_list) == 0:
            print("All of the host's certificates are valid !")
        else:
            print("Unfortunately, not all host's certificates are valid...")
            ca_cert = get_cert_file_content(config_yaml_dict['ca']['cert'])
            ca_key = get_cert_file_content(config_yaml_dict['ca']['key'])
            create_expired_certs(expired_certs_list, config_yaml_dict['bastion'], ca_cert, ca_key)

    except Exception as e:
        raise e
