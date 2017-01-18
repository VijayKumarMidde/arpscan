# ARP-SCAN
arp-scan.py is a simple network reconnaissance tool developed using Scapy framework.
In the script, I do a simple arp-ping to get the alive hosts list in a subnet, and 
print the MAC address and Vendor information of the IP

To get the vendor information, I am using the following REST API:
http://www.macvendorlookup.com/api/v2/{MAC_ADDRESS}

## Instructions to run
```
# For help menu
root@kali:~# python arp-scan.py -h

# Examples

## Get MAC info a single IP
root@kali:~# python arp-scan.py 192.168.0.100

## Get MAC info of all alive hosts in a subnet
root@kali:~# python arp-scan.py 192.168.0.0/24
```
