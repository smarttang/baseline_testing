#coding:utf-8
import re
import os

###################################
#
#	测试是否存在一些无关的账号
#
####################################

class TpassMod:
	global results
	results=[]
	def setBaseline_main(self,baseline_main):
		self.baseline_main=baseline_main

	def start(self):
		print "[*] Checking T_pass_Mod!!"
		black_list=['bin','daemon','adm','lp.sync.shutdown','halt','mail','news','uucp','operator','games','gopher','ftp','nobody','vcsa','oprofile','ntp','xfs','dbus','avahi','haldeamon','gdm','avahi-autoipd','sabayon','pcap']
		try:
			if os.path.exists("/etc/passwd"):
				obj_pw=open("/etc/passwd","r")
				for line in obj_pw:
					user_name=line.strip("\n").split(":")[0]
					try:
						black_list.index(user_name)
						results.append(user_name)
					except:
						pass
				obj_pw.close()
			else:
				pass
		except:
			pass

	def save(self):
		if len(results)>0:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-01","mod_name":"TpassMod","status":"1","results":str(results)})
		else:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-01","mod_name":"TpassMod","status":"0","results":"null"})
		print "[*] T_pass_Mod Finish!"

def getPluginClass():
	return TpassMod
