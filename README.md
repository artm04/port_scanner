# Port scanner #
It is a simple port scanner based on the built-in sockets library.
I created it for educational purposes, so it has quite a few features. But I am ready to accept any suggestions!

## How to use ##
```usage: scanner_cli.py [-h] [-v] [-p PORTS] [-f FILE] ip

Script for scanning devices for open ports

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


## Showcase ##
 ![Scanner showcase](.README_media/demo.gif)
