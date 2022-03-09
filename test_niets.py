import scanner as port_scanner


def test_port_scanner_invalid_hostname():
    err = port_scanner.get_open_ports("scanme.nmap", [22, 42], False)
    actual = err
    expected = "Error: Invalid hostname"

    assert actual == expected


def test_port_scanner_url_multiple_ports():
    ports = port_scanner.get_open_ports("scanme.nmap.org", [20, 81], False)
    actual = ports
    expected = [22, 80]

    assert actual == expected


def test_port_scanner_verbose_hostname_multiple_ports():
    str = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True)
    actual = str

    expected = "Open ports for scanme.nmap.org (45.33.32.156)\nPORT     SERVICE\n22       ssh\n80       http"
    assert actual == expected


def test_port_scanner_verbose_ip_hostname_returned_multiple_ports():
    str = port_scanner.get_open_ports("137.74.187.104", [440, 450], True)
    actual = str
    expected = "Open ports for hackthissite.org (137.74.187.104)\nPORT     SERVICE\n443      https"
    assert actual == expected


def test_port_scanner_verbose_ip_no_hostname_returned_single_port():
    str = port_scanner.get_open_ports("104.26.10.78", [440, 450], True)
    actual = str
    expected = "Open ports for 104.26.10.78\nPORT     SERVICE\n443      https"

    print(actual)

    assert actual == expected
