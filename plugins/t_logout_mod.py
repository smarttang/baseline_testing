#coding:utf-8
import re
import commands
import os

###################################
#
#	测试是否设置自动登出
#
####################################

class TlogoutMod:
	global results,sorce
	results=[]
	sorce=100
	def setBaseline_main(self,baseline_main):
		self.baseline_main=baseline_main

	def start(self):
		tmp_list=[]
		print "[*] Checking TlogoutMod!!"
		try:
			if os.path.exists("/etc/profile"):
				obj_r=open("/etc/profile","r")
				for line in obj_r:
					if re.search("export TMOUT=180;export TMOUT",line):
						sorce=sorce-10
				if sorce<100:
					results.append({"LoginOutTime":"Enable"})
				else:
					results.append({"LoginOutTime":"Distable"})
				obj_r.close()
			else:
				results.append({"LoginOutTime":"Distable"})
				print "[*] No Found profile!!"
		except:
			results.append({"LoginOutTime":"Distable"})
			

	def save(self):
		if results[0].get('LoginOutTime')=="Distable":
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-07","mod_name":"TlogoutMod","status":"1","results":str(results)})
		else:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-07","mod_name":"TlogoutMod","status":"0","results":"null"})
		print "[*] TlogoutMod Finish!"

def getPluginClass():
	return TlogoutMod

if __name__=="__main__":
	t=TlogoutMod()
	t.start()
	t.save()
