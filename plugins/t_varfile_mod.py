#coding:utf-8
import re
import commands

###################################
#
#	测试系统日志是否做了权限限制
#
####################################

class TvarfileMod:
	global results,sorce
	results=[]
	sorce=60
	def setBaseline_main(self,baseline_main):
		self.baseline_main=baseline_main

	def start(self):
		print "[*] Checking TvarfileMod!!"
		check_list=['/var/log/message','/var/log/secure','/var/log/maillog','/var/log/cron','/var/log/spooler','/var/log/boot.log']
		try:
			for item in check_list:
				if os.path.exists(item):
					test_com=commands.getoutput("ls -l "+item).split(" ")
					if not test_com[0]=="-rw-r-----":
						sorce=sorce-10
						results.append({item:test_com[0]})
		except:
			pass

		# print self.baseline_main.output_name
	def save(self):
		if sorce<60:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-06","mod_name":"TvarfileMod","status":"1","results":str(results)})
		else:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-06","mod_name":"TvarfileMod","status":"0","results":"null"})
		print "[*] TvarfileMod Finish!"

def getPluginClass():
	return TvarfileMod
