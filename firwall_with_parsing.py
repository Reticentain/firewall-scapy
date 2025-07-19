import random

#creating a list

def creating_network(network):

    network.append(f"192.168.1.{random.randint(1,100)}")
    return network

def taking_action(network):
    for ip in network:

        #we need to make ip to represent the first index of network (list)
        #after that we parsed the ip split will split it into "192" "168" "1" "75"
        #[-1] will get only the last index like 75

        ip_address = int(ip.split(".")[-1])
        if ip_address <= 20 and ip_address >= 0 :
            print(f"{ip} : Action taken: Block")
        elif ip_address <= 50 and ip_address > 20:
            print(f"{ip} : Action taken: Access")
        elif ip_address <= 90 and ip_address > 50:
            print(f"{ip} : Action taken: Check before passing")
        else:
            print(f"{ip} : Action taken: Suspicious: Terminate the Action")

def main():
    network = []
    for i in range (20):
        creating_network(network)
    taking_action(network)
main()




#network = ["192.168.1.12:allow", "192.168.1.10:block", "192.168.1.14:allow"]


