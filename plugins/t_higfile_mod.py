#coding:utf-8
import re
import os

###################################
#
#	测试是否存在敏感高危
#
####################################

class ThigfileMod:
	global results,sorce
	results=[]
	sorce=30
	def setBaseline_main(self,baseline_main):
		self.baseline_main=baseline_main

	def start(self):
		tmp_list=[]
		print "[*] Checking ThigfileMod!!"
		try:
			if os.path.exists("/.netrc"):
				sorce=sorce-10
				results.append({"high file netrc":"/.netrc"})

			if os.path.exists("/.rhosts"):
				sorce=sorce-10
				results.append({"high file rhosts":"/.rhosts"})

			if os.path.exists("/etc/hosts.equiv"):
				sorce=sorce-10
				results.append({"high file hosts.equiv":"/hosts.equiv"})
		except:
			pass

	def save(self):
		if sorce<30:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-10","mod_name":"ThigfileMod","status":"1","results":str(results)})
		else:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-10","mod_name":"ThigfileMod","status":"0","results":"null"})
		print "[*] ThigfileMod Finish!"

def getPluginClass():
	return ThigfileMod
