from scapy.all import *
import random

def making_packet(target, r):
    target.append(f"192.168.127.{random.randint(0,r)}")

def sending_packet(target):
    src_mac = RandMAC()
    dst_mac = RandMAC()

    for packet in target:
        pkt = Ether(dst=dst_mac, src= src_mac, type=0x0800)/IP(dst=packet, src= "192.168.1.1")/TCP(dport=80, flags='S')/ICMP()
        send(pkt)
        pkt.show()
def main():
    target = []

    times = int(input("How many packets do you want to send?"))
    ran = int(input("Enter the range in which you want to send the packets (1-255)"))
    pkt_type = input("Enter the type of packet you want to send: ").upper()

    if pkt_type == "ICMP" or "TCP" or "UDP" or "ARP":

        if ran <= 255 and ran >= 1:
            for i in range(times):
                making_packet(target, ran)
            sending_packet(target)

    else:
        print("Not an option, next time select from tcp, udp, arp, or icmp")
        quit()

if __name__ == '__main__':
    main()
