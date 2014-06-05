#coding:utf-8
import re
import commands

###################################
#
#	测试passwd和shadow的权限
#
####################################

class TpscomMod:
	global results
	results=[]
	def setBaseline_main(self,baseline_main):
		self.baseline_main=baseline_main

	def start(self):
		print "[*] Checking TpscomMod!!"
		try:
			passwd_com=commands.getoutput("ls -l /etc/passwd").split(" ")
			shadow_com=commands.getoutput("ls -l /etc/shadow").split(" ")
			group_com=commands.getoutput("ls -l /etc/group").split(" ")

			if not passwd_com[0]=="-rw-r--r--":
				if not passwd_com[2]=="root":
					if not passwd_com[3]=="root":
						results.append({"target":"/etc/passwd","password_purview":passwd_com[0],"user/group":passwd_com[2]+"/"+passwd_com[3]})
					else:
						results.append({"target":"/etc/passwd","password_purview":passwd_com[0],"user":passwd_com[2]})
				else:
					if not passwd_com[3]=="root":
						results.append({"target":"/etc/passwd","password_purview":passwd_com[0],"group":passwd_com[3]})
					else:
						results.append({"target":"/etc/passwd","password_purview":passwd_com[0]})
			else:
				if not passwd_com[2]=="root":
					if not passwd_com[3]=="root":
						results.append({"target":"/etc/passwd","user/group":passwd_com[2]+"/"+passwd_com[3]})
					else:
						results.append({"target":"/etc/passwd","user":passwd_com[2]})
				else:
					if not passwd_com[3]=="root":
						results.append({"target":"/etc/passwd","group":passwd_com[3]})
					else:
						pass

			if not shadow_com[0]=="-r--------":
				if not shadow_com[2]=="root":
					if not shadow_com[3]=="root":
						results.append({"target":"/etc/shadow","password_purview":shadow_com[0],"user/group":shadow_com[2]+"/"+shadow_com[3]})
					else:
						results.append({"target":"/etc/shadow","password_purview":shadow_com[0],"user":shadow_com[2]})
				else:
					if not shadow_com[3]=="root":
						results.append({"target":"/etc/shadow","password_purview":shadow_com[0],"group":shadow_com[3]})
					else:
						results.append({"target":"/etc/shadow","password_purview":shadow_com[0]})
			else:
				if not shadow_com[2]=="root":
					if not shadow_com[3]=="root":
						results.append({"target":"/etc/shadow","user/group":shadow_com[2]+"/"+shadow_com[3]})
					else:
						results.append({"target":"/etc/shadow","user":shadow_com[2]})
				else:
					if not shadow_com[3]=="root":
						results.append({"target":"/etc/shadow","group":shadow_com[3]})
					else:
						pass

			if not group_com[0]=="-rw-r--r--":
				if not group_com[2]=="root":
					if not group_com[3]=="root":
						results.append({"target":"/etc/group","password_purview":group_com[0],"user/group":group_com[2]+"/"+group_com[3]})
					else:
						results.append({"target":"/etc/group","password_purview":group_com[0],"user":group_com[2]})
				else:
					if not group_com[3]=="root":
						results.append({"target":"/etc/group","password_purview":group_com[0],"group":group_com[3]})
					else:
						results.append({"target":"/etc/group","password_purview":group_com[0]})
			else:
				if not group_com[2]=="root":
					if not group_com[3]=="root":
						results.append({"target":"/etc/group","user/group":group_com[2]+"/"+group_com[3]})
					else:
						results.append({"target":"/etc/group","user":group_com[2]})
				else:
					if not group_com[3]=="root":
						results.append({"target":"/etc/group","group":group_com[3]})
					else:
						pass
		except:
			pass

		# print self.baseline_main.output_name
	def save(self):
		if len(results)>0:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-04","mod_name":"TpscomMod","status":"1","results":str(results)})
		else:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-04","mod_name":"TpscomMod","status":"0","results":"null"})
		print "[*] TpscomMod Finish!"

def getPluginClass():
	return TpscomMod
