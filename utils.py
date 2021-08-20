"""Module contains unit for scanning IP address for open ports and parameter validation functions"""
import ipaddress
from argparse import ArgumentTypeError
from json import dump
from socket import socket


class Scanner:
    """Class for manipulating with specific IP address"""

    def __init__(self, ip, start_port, end_port):
        self.ip_address = ip
        self.start_port = start_port
        self.end_port = end_port
        self.open_ports = []

    def is_port_open(self, port):
        """Check if given port is open by initializing a connection"""
        sock = socket()
        sock.settimeout(3)
        try:
            sock.connect((self.ip_address, port))
            return True
        except ConnectionError:
            return False

    def scan_ports_range(self, output_filename=None):
        """Try to connect to every port in start_port->end_port range and return ports with successful connection"""
        opened = []
        for scanning_port in range(self.start_port, self.end_port):
            if self.is_port_open(scanning_port):
                opened.append(scanning_port)
        if output_filename:
            self.save_to_file(output_filename)
        return opened

    def save_to_file(self, filename):
        """Save scan report to a given file"""
        data = {
            'ip': self.ip_address,
            'ports_range': f'{self.start_port}-{self.end_port}',
            'opened_ports': self.open_ports}
        with open(filename, 'w') as info_file:
            dump(data, info_file, indent=4)


def valid_ip_address(ip: str):
    """Check if given address is a valid IPv4 address"""
    try:
        ipaddress.ip_address(ip)
        return ip
    except ValueError as e:
        raise ArgumentTypeError(f'invalid IP address: {ip}') from e


def valid_ports_range(ports: str):
    """Check if given ports range and ports in it are valid"""
    ports_range = list(map(int, ports.split('-')))
    if 1 <= ports_range[0] <= 65535 and 1 <= ports_range[1] <= 65535:
        return ports_range

    raise ArgumentTypeError(f'invalid ports range: {ports_range}')
