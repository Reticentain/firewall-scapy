from scapy.all import *
import random

def making_packet(target):
    target.append(f"192.168.127.{random.randint(0,255)}")

def sending_packet(target):
    for packet in target:
        pkt = Ether(dst="11:88:55:44:90:90", src="00:11:22:33:44:55", type=0x0800)/IP(dst=packet, src= "192.168.1.1")/TCP(dport=80, flags='S')/ICMP()
        send(pkt)
        pkt.show()
def main():
    target = []
    for i in range(10):
        making_packet(target)
    sending_packet(target)

if __name__ == '__main__':
    main()
