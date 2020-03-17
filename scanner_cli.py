#!/usr/bin/env python3
"""CLI app for port scanner"""
from argparse import ArgumentParser
import utils

__version__ = '1.0.0'

PARSER = ArgumentParser(
    description="Script for scanning devices for open ports")

PARSER.add_argument('-v', '--version', action='version',
                    version=f"{PARSER.prog}  {__version__} ")
PARSER.add_argument('ip', help="IP for scanning (example: 192.168.1.1)")
PARSER.add_argument('-p', '--ports', default='1-10000',
                    help="port range for scanning (example: 1-10000), default: 1-10000)")
PARSER.add_argument('-f', '--file', help="Save results to file")
ARGS = PARSER.parse_args()

IP = ARGS.ip
PORTS = list(map(int, ARGS.ports.split('-')))
FILE = ARGS.file

SCANNER = utils.Scanner(IP)
OPENED_PORTS = SCANNER.scan_ports_range(*PORTS, FILE)
print(f"IP: {IP}, ports: {PORTS[0]}->{PORTS[1]}")
print("Opened ports:", *OPENED_PORTS, sep="\n")
