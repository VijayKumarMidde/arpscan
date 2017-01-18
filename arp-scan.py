#! /usr/bin/env python

import argparse
import logging
import urllib2
import json
from scapy.all import *

def arpscan(target_ip):
    try:
        ans_pkts, unans_pkts = arping(target_ip, verbose=0)
        return [[ans_pkt[1].sprintf("%ARP.psrc%"), ans_pkt[1].sprintf("%Ether.src%"), \
                fetch_vendor_info(ans_pkt[1].sprintf("%Ether.src%"))] \
                for ans_pkt in ans_pkts]
    except Exception as e:
        print "Failed to get mac info. Did you provide correct IP/subnet? Error: {}".format(e)
        return []

def fetch_vendor_info(mac):
    url = "http://www.macvendorlookup.com/api/v2/%s" % mac
    try:
        data = json.load(urllib2.urlopen(url))
        return data[0]["company"]
    except Exception as e:
        return "Failed to fetch vendor info. Error: {}".format(e)

def print_summary(target, results):
    print "********* arp-scan report for %s *********" % target
    print "IP\t\tMAC\t\t\tVendor"
    print "-----------------------------------------------------"
    for result in results:
        print "%s\t%s\t%s" % (result[0], result[1], result[2])

def main():
    parser = argparse.ArgumentParser(description="arp-scan gets mac address and mac vendor info of a given ip or subnet")
    parser.add_argument("target", help="target ip or subnet. Ex: 192.168.0.0/24")
    args = parser.parse_args()
   
    ip = args.target
   
    #logging.getLogger("scapy").setLevel(2)
    print_summary(ip, arpscan(ip))

if __name__ == "__main__":
    main()


