import socket #  library allows script to communicate with other machines using TCP & UDP protocols
import termcolor #  used just to print statements in different colors


# concat function
def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)


# base port scanning function
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        print("[-] Port Closed " + str(port))

# target IP addresses, allowing for multiple entries
targets = input("[*] Enter Targets To Scan (seperate with ,): ")

# number of ports from 1 to input value
ports = input("[*] Enter How Many Ports You Want To Scan: ")

# split the IP addresses and strip spaces if multiple
if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)
