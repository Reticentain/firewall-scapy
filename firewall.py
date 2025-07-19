import random
def generate_ip():
    return f"192.169.1.{random.randint(1,20)}"

def check_rules(ip, rules):
    for ip_address in rules:
        if ip == ip_address:
            return rules[ip_address]
    else:
        return "allow"

def main():

    firewall_rules = {
        "192.169.1.1" : "block",
        "192.169.1.12": "block",
        "192.169.1.13": "block",
        "192.169.1.14": "block",
        "192.169.1.15": "block",
        "192.169.1.16": "block",
        "192.169.1.17": "block",
    }
    for i in range(12):
        ip_address = generate_ip()
        action =  check_rules (ip_address, firewall_rules)
        print(action)

main()


