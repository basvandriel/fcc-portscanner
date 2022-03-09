import re


def is_ip(address: str) -> bool:
    """
    Simply look for the four parts of the address
    """
    match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", address)

    return bool(match)
