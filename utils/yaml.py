import yaml

def get_dict_from_yaml_file(yaml_file_path: str) -> dict:
    with open(yaml_file_path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise exc

