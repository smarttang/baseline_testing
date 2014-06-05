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
		print "[*] Checking TbannerMod!!"
		try:
			obj_r=open("/etc/rc.d/rc.local","r")
			for line in obj_r:
				if re.match("^echo",line):
					tmp_list.append(line)

			if not len(tmp_list)>0:
				results.append({"Banner":str(tmp_list)})

			if os.path.exists("/etc/issue"):
				results.append({"Issue":"/etc/issue"})

			if os.path.exists("/etc/issue.net.bak"):
				results.append({"Issue.net":"/etc/issue.net"})
		except:
			pass

		# print self.baseline_main.output_name
	def save(self):
		if len(results)>0:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-09","mod_name":"TbannerMod","status":"1","results":str(results)})
		else:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-09","mod_name":"TbannerMod","status":"0","results":"null"})
		print "[*] TbannerMod Finish!"

def getPluginClass():
	return TbannerMod
