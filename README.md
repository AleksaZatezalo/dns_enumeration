# DNS Enumeration Tool

A Python-based DNS enumeration tool that allows you to discover and analyze DNS records and subdomains for a given domain.

## Features

- DNS record resolution (A, AAAA, MX, NS, TXT records)
- Subdomain enumeration using customizable wordlists
- Built-in wordlist generator with common subdomain names
- Interactive command-line interface

## Prerequisites

- Python 3.6 or higher
- dnspython library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/dns-enumeration-tool.git
cd dns-enumeration-tool
```

2. Install the required dependencies:
```bash
pip install dnspython
```

## Usage

Run the script:
```bash
python dns_enum.py
```

The tool provides two main functions:

1. Generate a subdomain wordlist:
   - Creates a file containing common subdomain names
   - Customizable output file name

2. Perform DNS enumeration:
   - Resolves various DNS record types
   - Discovers subdomains using a wordlist
   - Displays results in a readable format

### Example Usage

```bash
# Generate a wordlist
python dns_enum.py
> Select option 1
> Enter filename (or press Enter for default)

# Perform enumeration
python dns_enum.py
> Select option 2
> Enter domain (e.g., example.com)
> Enter wordlist path
```

## Sample Output

```
A Records:
  93.184.216.34

MX Records:
  mail.example.com (Priority: 10)

Subdomains found:
[+] Found subdomain: www.example.com
[+] Found subdomain: mail.example.com
[+] Found subdomain: api.example.com
```

## Security Considerations

This tool is intended for legitimate security testing and network administration purposes. Always ensure you have permission to perform DNS enumeration on the target domain.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on contributing to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
