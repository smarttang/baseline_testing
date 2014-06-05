#coding:utf-8
import re
import os

############################################
#
#	测试是否限制超级管理员远程登录
#	(要求必须先以普通用户登录，再升级到超级管理员)
#
############################################

class TsshMod:
	global results
	results=[]
	def setBaseline_main(self,baseline_main):
		self.baseline_main=baseline_main

	def start(self):
		pts_list=[]
		print "[*] Checking SShd config ...Wait!!"
		try:
			if os.path.exists("/etc/ssh/sshd_config"):
				obj_r=open("/etc/ssh/sshd_config","r")
				for line in obj_r:
					if re.match("^PermitRootLogin",line):
						Permit_value=line.split(" ")[1].strip("\n")
						if not Permit_value=="on":
							results.append({"PermitRootLogin":Permit_value})
					elif re.match("^#PermitRootLogin",line):
						results.append({"PermitRootLogin":"disable"})
					else:
						pass
				obj_r.close()
			else:
				print "[*] No Found sshd_config!!"

			if os.path.exists("/etc/securetty"):
				obj_r=open("/etc/securetty","r")
				for line in obj_r:
					if re.match("^pts",line):
						pts_list.append(line.strip("\n"))
					else:
						pass
				obj_r.close()
				if len(pts_list)==0:
					results.append({"LocalRootLogin":"disable"})
			else:
				print "[*] No Found securetty!!"
		except:
			pass

	def save(self):
		if len(results)>0:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-05","mod_name":"TloginMod","status":"1","results":str(results)})
		else:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-05","mod_name":"TloginMod","status":"0","results":"null"})
		print "[*] TsshMod Finish!"

def getPluginClass():
	return TsshMod
