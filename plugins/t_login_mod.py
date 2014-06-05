#coding:utf-8
import re
import commands
import os

###################################
#
#	1、测试用户密码生存周期
#	2、测试默认权限
#
####################################

class TloginMod:
	global results
	results=[]
	def setBaseline_main(self,baseline_main):
		self.baseline_main=baseline_main

	def start(self):
		print "[*] Checking T_login_Mod!!"
		try:
			if os.path.exists("/etc/login.defs"):
				obj_pw=open("/etc/login.defs","r")
				for line in obj_pw:
					if re.match("^PASS_MAX_DAYS",line):
						Pass_max_value=line.split("\t")[1].strip("\n")
						if not Pass_max_value=="90":
							results.append({"Pass_Max_Days":Pass_max_value})
				obj_pw.close()

				umask=commands.getoutput("cat /etc/login.defs |grep 'UMASK'").split("           ")
				if not umask[1]=="027":
					results.append({"UMASK":umask[1]})
			else:
				print "[*] No Found login.deffs!!"
		except:
			pass

		# print self.baseline_main.output_name
	def save(self):
		if len(results)>0:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-03","mod_name":"TloginMod","status":"1","results":str(results)})
		else:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-03","mod_name":"TloginMod","status":"0","results":"null"})
		print "[*] T_login_Mod Finish!"

def getPluginClass():
	return TloginMod
