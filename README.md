# Port scanner #
It is a simple port scanner based on the built-in sockets library.
I created it for educational purposes, so it has quite a few features. But I am ready to accept any suggestions!

## How to use ##
```
usage: scanner_cli.py [-h] [-v] [-p PORTS] [-f FILE] ip

positional arguments:
  ip                    IP for scanning (example: 192.168.1.1)

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -p PORTS, --ports PORTS
                        port range for scanning (example: 1-10000), default: 1-10000)
  -f FILE, --file FILE  Save results to file
 ```
### Arguments ###
`ip` - IP adress to scan. Example: `192.168.1.102`

`-p PORTS, --ports PORTS` - Port range. Specified using the `first-last` syntax. Default value is `1-10000`.

`-f FILE, --file FILE` - The name to save the file in JSON format with information about open ports, if specified.

### Examples ###
`$ scanner_cli.py 192.168.1.1 -p 80-8080` - scan IP 192.168.1.1 for open port in range from 80 to 8080

`$ scanner_cli.py 142.250.180.238 --ports 20-1000 --file scan.json` - scan IP 142.250.180.23 for open port in range from 20 to 1000 and save results to `scan.json` file

## Showcase ##

### Scan 192.168.1.1 for opened ports from 1 to 8080
[![asciicast](https://asciinema.org/a/DrPtCmGSE6pWWoYKFdwzPymmt.svg)](https://asciinema.org/a/DrPtCmGSE6pWWoYKFdwzPymmt)
### Same, but save results to JSON file ###
[![asciicast](https://asciinema.org/a/6nJ3YnF6rm4Mq3mqi4vqIzZHX.svg)](https://asciinema.org/a/6nJ3YnF6rm4Mq3mqi4vqIzZHX)