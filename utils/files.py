def get_cert_file_content(cert_path: str) -> str:
    with open(cert_path) as file:
        content = file.read()
    return content