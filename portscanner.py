import socket #  library allows script to communicate with other machines using TCP & UDP protocols


# concat function
def scan(target, ports):
    print('\n' + 'Starting Scan For ' + str(target))
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
        pass


print('''
.__            . __      .     .__        ,    __.                  
[__) _ .    , _|/  ` _  _| _   [__) _ ._.-+-  (__  _. _.._ ._  _ ._.
|  \(/, \/\/ (_]\__.(_)(_](/,  |   (_)[   |   .__)(_.(_][ )[ )(/,[  
                                                                    
'''
)

# target IP addresses, allowing for multiple entries
targets = input("[*] Enter Targets To Scan (seperate with ,): ")

# number of ports from 1 to input value, added one additional port to make sure last port is also scanned
ports = 1 + int(input("[*] Enter How Many Ports You Want To Scan: "))

# split the IP addresses and strip spaces if multiple
if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)
