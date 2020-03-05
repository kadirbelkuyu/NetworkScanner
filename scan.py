import scapy.all as scapy
import pprint

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answerd_list = scapy.srp(arp_request_broadcast, timeout=1)[0]

    for element in answerd_list:
        print(element)
        print("------------------------------------------------------")

    

scan("192.168.0.1/24")
