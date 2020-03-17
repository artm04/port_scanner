""" Objects and fuctions for port scanner """

from socket import socket
from json import dump


class Scanner:
    """ Port scanner class """

    def __init__(self, ip):
        self.ip_address = ip

    def is_port_open(self, port):
        """ Check if port is open """
        sock = socket()
        sock.settimeout(3)
        try:
            sock.connect((self.ip_address, port))
            return True
        except ConnectionError:
            pass

    def scan_ports_range(self, start, stop, output_filename=None):
        """ Get open ports in range """
        opened = []
        for scanning_port in range(start, stop):
            if self.is_port_open(scanning_port):
                opened.append(scanning_port)
        if output_filename:
            data = {
                'ip': self.ip_address,
                'ports_range': f'{start}-{stop}',
                'opened_ports': opened}
            dump(data, open(output_filename, 'w'), indent=4)
        return opened
