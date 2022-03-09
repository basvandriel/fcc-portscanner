import re
import socket

from is_ip import is_ip
from is_open import is_open

from common_ports import ports_and_services

# The number of spaces between table headers
GAP = " " * 5


def get_open_ports(target, port_range, verbose: bool = False):
    open_ports = []
    valid_ip: bool = is_ip(target)

    # Add the ip after the name by default
    add_ip_hint = True

    try:
        ip: str = socket.gethostbyname(target)
    except OSError:
        unit = "hostname" if not valid_ip else "IP address"
        return f"Error: Invalid {unit}"

    host = target

    try:
        host = socket.gethostbyaddr(target)[0] if valid_ip else target
    except:
        add_ip_hint = False

    banner: str = f"Open ports for {host}"

    if add_ip_hint:
        banner += f" ({ ip })"

    # And add the table headers
    banner += f"\nPORT{GAP}SERVICE"

    for port in range(port_range[0], port_range[1] + 1):
        if not is_open(ip, port):
            continue

        # Yeah we need to keep track
        curr_gap = GAP

        open_ports.append(port)
        service = ports_and_services.get(port)

        # It needs some more space when only 2 digits
        if port < 100:
            curr_gap += "  "

        if port > 100:
            curr_gap += " "

        # added 2 spaces
        banner += f"\n{port}{curr_gap}{service}"

    return (open_ports) if not verbose else banner
