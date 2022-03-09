import socket


def is_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        s.connect((ip, int(port)))
        s.shutdown(2)

        s.close()
        return True
    except:
        s.close()
        return False
