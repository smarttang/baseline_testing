#coding:utf-8
import re
import commands

###################################
#
#	测试用户Home目录权限
#
####################################

class TcompetMod:
	global results
	results=[]
	def setBaseline_main(self,baseline_main):
		self.baseline_main=baseline_main

	def start(self):
		print "[*] Checking T_compet_Mod!!"

		obj_pw=open("/etc/passwd","r")
		for line in obj_pw:
			try:
				directory_name=line.strip("\n").split(":")[-2]
				user_name=line.strip("\n").split(":")[0]
				_text=commands.getstatusoutput(str(directory_name))
				if re.match("^ls",_text):
					pass
				else:
					directory_compet=_text.split(" ")[0]
					if not re.match("^drwxr-x---",directory_compet):
						results.append({"username":user_name,"compet":directory_compet,"home_directory":directory_name})
			except:
				pass
		obj_pw.close()
	def save(self):
		if len(results)>0:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-02","mod_name":"TcompetMod","status":"1","results":str(results)})
		else:
			self.baseline_main.xml_result({"mod_id":"37wan-cent0S-02","mod_name":"TcompetMod","status":"0","results":"null"})
		print "[*] T_compet_Mod Finish!"

def getPluginClass():
	return TcompetMod

if __name__ == '__main__':
	a=TcompetMod()
	a.start()
	a.save()