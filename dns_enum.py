import dns.resolver
import socket
# Function to resolve DNS records
def resolve_dns(domain):
    records = {
        'A': [],
        'AAAA': [],
        'MX': [],
        'NS': [],
        'TXT': []
    }
    try:
        # A records
        answers = dns.resolver.resolve(domain, 'A')
        records['A'] = [answer.to_text() for answer in answers]
    except Exception as e:
        print(f"No A records found for {domain}: {e}")
    try:
        # AAAA records
        answers = dns.resolver.resolve(domain, 'AAAA')
        records['AAAA'] = [answer.to_text() for answer in answers]
    except Exception as e:
        print(f"No AAAA records found for {domain}: {e}")
    try:
        # MX records
        answers = dns.resolver.resolve(domain, 'MX')
        records['MX'] = [f"{answer.exchange} (Priority: {answer.preference})" for answer in answers]
    except Exception as e:
        print(f"No MX records found for {domain}: {e}")
    try:
        # NS records
        answers = dns.resolver.resolve(domain, 'NS')
        records['NS'] = [answer.to_text() for answer in answers]
    except Exception as e:
        print(f"No NS records found for {domain}: {e}")
    try:
        # TXT records
        answers = dns.resolver.resolve(domain, 'TXT')
        records['TXT'] = [answer.to_text() for answer in answers]
    except Exception as e:
        print(f"No TXT records found for {domain}: {e}")
    return records
# Function to enumerate subdomains
def enumerate_subdomains(domain, wordlist_file):
    subdomains = []
    try:
        with open(wordlist_file, 'r') as f:
            subdomain_list = f.read().splitlines()
            for sub in subdomain_list:
                subdomain = f"{sub}.{domain}"
                try:
                    socket.gethostbyname(subdomain)
                    print(f"[+] Found subdomain: {subdomain}")
                    subdomains.append(subdomain)
                except socket.gaierror:
                    pass  # Subdomain does not exist
    except FileNotFoundError:
        print(f"Wordlist file {wordlist_file} not found!")
    return subdomains
# Function to generate a wordlist
def generate_wordlist(file_name="subdomains.txt"):
    # Common subdomains for enumeration
    common_subdomains = [
        "www", "mail", "ftp", "api", "webmail", "vpn", "test", "dev", "portal",
        "admin", "intranet", "blog", "secure", "shop", "support", "docs",
        "forum", "news", "status", "mobile", "dashboard", "cdn", "static",
        "staging", "beta", "app", "files", "cloud", "mysql", "node", "server"
    ]
    try:
        with open(file_name, "w") as f:
            for subdomain in common_subdomains:
                f.write(subdomain + "\n")
        print(f"[+] Wordlist saved to {file_name}")
    except Exception as e:
        print(f"[-] Failed to write wordlist: {e}")
if name == "main":
    print("[1] Generate a subdomain wordlist")
    print("[2] Perform DNS enumeration")
    choice = input("Enter your choice: ")
    if choice == "1":
        output_file = input("Enter the file name for the wordlist (default: subdomains.txt): ")
        if not output_file.strip():
            output_file = "subdomains.txt"
        generate_wordlist(output_file)
    elif choice == "2":
        domain = input("Enter the domain to enumerate: ")
        wordlist = input("Enter the path to the subdomain wordlist: ")
        print("\n[] Resolving DNS records...")
        dns_records = resolve_dns(domain)
        for record_type, values in dns_records.items():
            print(f"\n{record_type} Records:")
            for value in values:
                print(f"  {value}")
        print("\n[] Enumerating subdomains...")
        subdomains = enumerate_subdomains(domain, wordlist)
        print("\nSubdomains found:")
        for sub in subdomains:
            print(sub)
    else:
        print("Invalid choice. Exiting.")
