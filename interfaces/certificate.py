from datetime import datetime


class CertificateFile:
    def __init__(self, file_path: str,host_user: str = None,host: str = None, expiration_date: datetime = None):
        self.host = host
        self.host_user = host_user
        self.file_path = file_path
        self.expiration_date = expiration_date

    def set_expiration_date(self, expiration_date: datetime):
        self.expiration_date = expiration_date
