#!/usr/bin/python3

bad = "\033[91m[-]\033[00m"

import requests
import time
import argparse
import re
import os
import sys
import ssl
from urllib.parse import urlparse
from colorama import init, Fore, Back, Style
from func import path_only,params_only,attack
from os.path import exists



def banner():
    print(("""%s
  _            __  __         __   ___  
 | |          / _|/ _|       /_ | / _ \ 
 | |    _   _| |_| |_ _   _   | || | | |
 | |   | | | |  _|  _| | | |  | || | | |
 | |___| |_| | | | | | |_| |  | || |_| |
 |______\__,_|_| |_|  \__, |  |_(_)___/ 
                       __/ |            
                      |___/             
                                                              %s%s
        # Coded By winteriscoming - f.b0naprta@gmail.com%s
    """ % ('\033[91m', '\033[0m', '\033[93m', '\033[0m')))

banner()
def parser_error(errmsg):
	print(("Usage: python3 " + sys.argv[0] + " -f URLS_FILE -p PAYLOADS-FILE"))
	print(("Error: " + errmsg))
	sys.exit()

def parse_args():
	parser = argparse.ArgumentParser()
	parser.error = parser_error
	parser.add_argument('-f', help='urls file', dest='urls')
	parser.add_argument('-p', help='payloads file', dest='payloads', default='payloads.txt')
	args = parser.parse_args()
	urls = args.urls
	payloads = args.payloads
	if not (args.urls or args.payloads):
		parser_error("urls or payloads flags are not provided")
	if urls and not os.path.isfile(urls):
		parser.error("input file " + urls + " doesn't exist.")
	if not urls:
		parser.error("please provide the input file!")
	if payloads and not os.path.isfile(payloads):
		parser.error("payloads file " + payloads + " doesn't exist.")

	return args

args = parse_args()

##########################################

urls_file = open(args.urls).read().splitlines()
payloads_file = open(args.payloads).read().splitlines()

for url in urls_file:
	if ("&" or "=" or "?") not in url:
		for i in path_only(url):
			for p in payloads_file:
				x = i.replace('PAYLOAD',p)
				attack(x)
	
	elif (url.count("/") > 3 and "?" in url):
		for i in path_only(url):
			for p in payloads_file:
				x = i.replace('PAYLOAD',p)
				attack(x)
		for i in params_only(url):
			for p in payloads_file:
				x = i.replace('PAYLOAD',p)
				attack(x)
	else:
		for i in params_only(url):
			for p in payloads_file:
				x = i.replace('PAYLOAD',p)
				attack(x)