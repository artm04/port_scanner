#!/usr/bin/env python3
"""CLI app for port scanner"""
from argparse import ArgumentParser
import utils

__version__ = '1.0.0'

parser = ArgumentParser(
    description="Script for scanning devices for open ports")
parser.add_argument('-v', '--version', action='version',
                    version=f"{parser.prog}  {__version__} ")
parser.add_argument('ip', help="IP for scanning (example: 192.168.1.1)")
parser.add_argument('-p', '--ports', default='1-10000',
                    help="port range for scanning (example: 1-10000), default: 1-10000)")
parser.add_argument('-f', '--file', help="Save results to file")

args = parser.parse_args()

# TODO add ports range and IP validation
ip = args.ip
ports = list(map(int, args.ports.split('-')))
file = args.file

scanner = utils.Scanner(ip)
opened_ports = scanner.scan_ports_range(*ports, file)
print(f"IP: {ip}, ports: {ports[0]}->{ports[1]}")
print("Opened ports:", *opened_ports, sep="\n")
