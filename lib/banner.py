#!/usr/bin/env python

from lib.colors import *

class Banner:
	def banner(self):
		print("_"*40)
		print(" -[ CobWEB Email OSINT Tool")
		print(" -[ Made by yuh bois Crypto up in dis joint")
		print(" -[ %sAs said in a quote 'you can run but you cannot hide'%s "%(Y%0,E))
		print("_"*40 + "\n")

	def usage(self,_exit_=False):
		self.banner()
		print("Usage: cobweb.py [OPTIONS]\n")
		print("\t-d --domain\tTarget URL/Name... whatever")
		print("\t-s --source\tData source, default \"all\":\n")
		print("\t\tall\tUse all search engines")
		print("\t\tgoogle\tUse google search engine")
		print("\t\tbing\tUse bing search engine")
		print("\t\tyahoo\tUse yahoo search engine")
		print("\t\task\tUse ask search engine")
		print("\t\tbaidu\tUse baidu search engine")
		print("\t\tdogpile\tUse dogpile search engine")
		print("\t\texalead\tUse exalead search engine")
		print("\t\tpgp\tUse pgp search engine\n")
		print("\t-b --breach-check\tCheck if email was or is breached")
		print("\t-o --osint\tGet email information or IPs")
		print("\t-r --report\tSimple file text report")
		print("\t-v --verbose\tVerbosity level (1,2 or 3)")
		print("\t-H --help\tShow this help and exit\n")
		print("Example:")
		print("\tcobweb.py --domain example.com -v 3")
		print("\tcobweb.py --osint admin@site.com -v 3")
		print("\tcobweb.py --domain example.com --source pgp --breach-check -v 1")
		print("\tcobweb.py --domain example.com --source google --breach-check --report example.txt -v 3\n")
		if _exit_: exit(0)
