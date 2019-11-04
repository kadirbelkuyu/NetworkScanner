#add library
import scapy.all as scapy

#scan method 
def scan(ip):
    scapy.arping(ip)#scan come ip

scan("192.168.0.1/24") #call scan method with ip args 
