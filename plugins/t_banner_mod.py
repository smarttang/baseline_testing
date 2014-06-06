#coding:utf-8
import re
import os

###################################
#
#	测试是否存在系统信息泄露的问题
#
####################################

class TbannerMod:
	global results
	results=[]
	def setBaseline_main(self,baseline_main):
		self.baseline_main=baseline_main

	def start(self):
		tmp_list=[]
		sorce=10
		print "[*] Checking TbannerMod!!"
		try:
			if os.path.exists("/etc/rc.d/rc.local"):
				obj_r=open("/etc/rc.d/rc.local","r")
				for line in obj_r:
					if re.match("^echo",line):
						sorce=sorce-1
						tmp_list.append(line)
				if sorce<10:
					results.append({"Banner":str(tmp_list)})
				obj_r.close()

			if os.path.exists("/etc/issue"):
				results.append({"Issue":"/etc/issue"})

			if os.path.exists("/etc/issue.net.bak"):
				results.append({"Issue.net":"/etc/issue.net"})
		except:
			pass

	def save(self):
		if len(results)>0:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-09","mod_name":"TbannerMod","status":"1","results":str(results)})
		else:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-09","mod_name":"TbannerMod","status":"0","results":"null"})
		print "[*] TbannerMod Finish!"

def getPluginClass():
	return TbannerMod
