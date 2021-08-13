""" Objects and functions for port scanner """
from json import dump
from socket import socket


class Scanner:
    """ Port scanner class """

    def __init__(self, ip, start_port, end_port):
        self.ip_address = ip
        self.start_port = start_port
        self.end_port = end_port
        self.open_ports = []

    def is_port_open(self, port):
        """ Check if port is open """
        sock = socket()
        sock.settimeout(3)
        try:
            sock.connect((self.ip_address, port))
            return True
        except ConnectionError:
            return False

    def scan_ports_range(self, output_filename=None):
        """ Get open ports in range """
        opened = []
        for scanning_port in range(self.start_port, self.end_port):
            if self.is_port_open(scanning_port):
                opened.append(scanning_port)
        if output_filename:
            self.save_to_file(output_filename)
        return opened

    def save_to_file(self, filename):
        data = {
            'ip': self.ip_address,
            'ports_range': f'{self.start_port}-{self.end_port}',
            'opened_ports': self.open_ports}
        with open(filename, 'w') as info_file:
            dump(data, info_file, indent=4)
