#!/usr/bin/env python

from lib.output import *
from lib.request import *
from lib.parser import *

class Google(Request):
	def __init__(self,target):
		Request.__init__(self)
		self.target = target

	def search(self):
		test('Searching "%s" in Google...'%(self.target))
		url = "https://www.google.it/search?num=1000&hl=en&q=%40{target}".format(
			target=self.target)
		try:
			resp = self.send(
				method = 'GET',
				url = url
				)
			return self.getemail(resp.content,self.target)
		except Exception as e:
			pass

	def getemail(self,content,target):
		return parser(content,target).email()
