#coding:utf-8
import commands

###################################
#
#	测试开放的端口
#
####################################

class TportMod:
	global results
	results=[]
	def setBaseline_main(self,baseline_main):
		self.baseline_main=baseline_main

	def start(self):
		print "[*] Checking T_port_Mod!!"
		try:
			results=commands.getoutput("netstat -atnp|awk '{print $4}'|grep '0.0.0.0:' |awk -F: '{print $2}'").split("\n")
		except:
			pass

	def save(self):
		if len(results)>0:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-11","mod_name":"TportMod","status":"1","results":str(results)})
		else:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-11","mod_name":"TportMod","status":"0","results":"null"})
		print "[*] T_port_Mod Finish!"

def getPluginClass():
	return TportMod