#coding:utf-8
import re
import commands

###################################
#
#	1、测试FTP账号是否存在违禁账号
#	2、测试是否禁止了ROOT用户FTP登录
#	3、测试是否禁止匿名登录
#
####################################

class TftpMod:
	global results
	results=[]
	def setBaseline_main(self,baseline_main):
		self.baseline_main=baseline_main

	def start(self):
		ftpuser_bool=False
		ftpconf_bool=False
		black_list=['bin','daemon','adm','lp.sync.shutdown','halt','mail','news','uucp','operator','games','gopher','ftp','nobody','vcsa','oprofile','ntp','xfs','dbus','avahi','haldeamon','gdm','avahi-autoipd','sabayon','pcap']
		print "[*] Checking TftpMod!!"
		try:
			obj_r=open("/etc/vsftpd/chroot_list","r")
			for line in obj_r:
				try:
					black_list.index(line.strip("\n"))
					results.append(line.strip("\n"))
				except:
					pass
			obj_r.close()

			obj_r=open("/etc/vsftpd/ftpusers","r")
			for line in obj_r:
				if re.match("^root",line):
					ftpuser_bool=True
			if ftpuser_bool==False:
				results.append({"File_path":"/etc/vsftpd/ftpusers","user":"root"})
			obj_r.close()

			obj_r=open("/etc/vsftpd/vsftd.conf","r")
			for line in obj_r:
				if re.match("^anonymous_enable=NO",line):
					ftpconf_bool=True
			if ftpconf_bool==False:
				results.append({"File_path":"/etc/vsftpd/vsftd.conf","anonymous_enable":"Enable"})
			obj_r.close()
		except:
			pass

	def save(self):
		if len(results)>0:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-08","mod_name":"TftpMod","status":"1","results":str(results)})
		else:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-08","mod_name":"TftpMod","status":"0","results":"null"})
		print "[*] TftpMod Finish!"

def getPluginClass():
	return TftpMod
