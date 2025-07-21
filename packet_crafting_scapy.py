from scapy.all import *
import random

def making_packet(target, r):
    target.append(f"192.168.127.{random.randint(0,r)}")

def sending_packet(target, type_packet):
    src_mac = RandMAC()
    dst_mac = RandMAC()
    for packet in target:
        if type_packet == "ARP":
            pkt = Ether(dst=dst_mac, src= src_mac)/ARP(pdst=packet)
        elif type_packet == "TCP":
            pkt = Ether(dst=dst_mac, src= src_mac, type=0x0800)/IP(dst=packet, src= "192.168.1.1")/TCP(dport=80, flags='S')
        elif type_packet =="ICMP":
            pkt = Ether(dst = dst_mac, src = src_mac)/IP(dst= packet)/ICMP()
        else:
            pkt = Ether(dst = dst_mac, src = src_mac)/IP(dst = packet, src = "192.168.1.1")/UDP(dport = random.randint(1,50), sport = random.randint(1,50))
        send(pkt)
        pkt.show()

def main():
    target = []

    times = int(input("How many packets do you want to send?"))
    ran = int(input("Enter the range in which you want to send the packets (1-255)"))
    pkt_type = input("Enter the type of packet you want to send: ").upper()

    if pkt_type in ["ICMP","TCP","UDP","ARP"]:

        if ran <= 255 and ran >= 1:
            for i in range(times):
                making_packet(target, ran)
            sending_packet(target, pkt_type)
        else:
            print("It should be between 1 and 255")
            quit()
    else:
        print("Not an option, next time select from tcp, udp, arp, or icmp")
        quit()

if __name__ == '__main__':
    main()
