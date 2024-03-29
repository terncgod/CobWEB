#!/usr/bin/env python

from lib.output import *
from lib.request import *
from lib.parser import *

class Shodan(Request):
	def __init__(self,ip):
		Request.__init__(self)
		self.ip = ip

	def search(self):
		url = "https://api.shodan.io/shodan/host/{target}?key=UNmOjxeFS2mPA3kmzm1sZwC0XjaTTksy".format(
			target=self.ip)
		try:
			resp = self.send(
				method = 'GET',
				url = url
				)
			if resp.status_code != 200: return b'{}'
			return resp.content
		except Exception as e:
			pass
