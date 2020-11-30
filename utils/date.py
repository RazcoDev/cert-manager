from datetime import datetime


def convert_pem_date_to_datetime(pem_date: str) -> datetime:
    try:
        date_without_timezone = ' '.join(pem_date.split(' ')[:-1])
        return datetime.strptime(date_without_timezone, '%b %d %X %Y')
    except Exception as e:
        print("Could not convert date to datetime")
        raise e


def is_expiration_date_due(expiration_date: datetime) -> bool:
    return expiration_date > datetime.now()
