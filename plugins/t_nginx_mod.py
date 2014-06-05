#coding:utf-8
import re
import os

###################################
#
#	测试nginx配置安全
#
####################################

# 清除空格函数
def clean_str(sttr):
	_result=[]
	for item in sttr.split(" "):
		if item.strip():
			_result.append(item.strip())
	return _result


class TnginxMod:
	global results,sorce
	results=[]
	sorce=100
	def setBaseline_main(self,baseline_main):
		self.baseline_main=baseline_main

	def start(self):
		check_path='/usr/local/nginx/conf/nginx.conf'
		print "[*] Checking TnginxMod!!"
		try:
			if os.path.exists(check_path):
				obj_r=open(check_path,"r")
				for line in obj_r:
					#####################################
					#
					#        控制缓冲区溢出攻击
					#
					#####################################
					# client_body_buffer_size 指定连接请求实体的缓冲区大小
					if re.search("client_body_buffer_size",line):
						client_body_buffer_size=clean_str(line)
						if not client_body_buffer_size[1]=="1k;":
							sorce=sorce-14
							results.append({'client_body_buffer_size':client_body_buffer_size[1]})

					# client_header_buffer_size 指定客户端请求头部的缓冲区大小
					elif re.search("client_header_buffer_size",line):
						client_header_buffer_size=clean_str(line)
						if not client_header_buffer_size[1]=="1k;":
							sorce=sorce-14
							results.append({'client_header_buffer_size':client_header_buffer_size[1]})

					# client_max_body_size 指定允许客户端连接的最大请求实体大小		
					elif re.search("client_max_body_size",line):
						client_max_body_size=clean_str(line)
						if not client_max_body_size[1]=="1k;":
							sorce=sorce-14
							results.append({'client_max_body_size':client_max_body_size[1]})

					# large_client_header_buffers 指定客户端一些比较大的请求头使用的缓冲区数量和大小
					elif re.search("large_client_header_buffers",line):
						large_client_header_buffers=clean_str(line)
						if not large_client_header_buffers[2]=="1k;" and large_client_header_buffers[1]=='2':
							sorce=sorce-14
							results.append({'large_client_header_buffers_option1':large_client_header_buffers[1],'large_client_header_buffers_option2':large_client_header_buffers[2]})

					#####################################
					#
					#        控制超时提高性能
					#
					#####################################
					# client_body_timeout  指定读取请求实体的超时时间
					elif re.search('client_body_timeout',line):
						client_body_timeout=clean_str(line)
						if not client_body_timeout[1]=="10":
							sorce=sorce-11
							results.append({'client_body_timeout':client_body_timeout[1]})

					# client_header_timeout 指定读取客户端请求头标题的超时时间
					elif re.search('client_header_timeout',line):
						client_header_timeout=clean_str(line)
						if not client_header_timeout[1]=="10":
							sorce=sorce-11
							results.append({'client_header_timeout':client_header_timeout[1]})

					# keepalive_timeout 参数的第一个值指定了客户端与服务器长连接的超时时间，超过这个时间，服务器将关闭连接。参数的第二个值（可选）指定了应答头中Keep-Alive: timeout=time的time值。
					elif re.search('keepalive_timeout',line):
						keepalive_timeout=clean_str(line)
						if not keepalive_timeout[1]=="5" and keepalive_timeout[2]=="5":
							sorce=sorce-11
							results.append({'keepalive_timeout_option1':keepalive_timeout[1],'keepalive_timeout_option2':keepalive_timeout[2]})

					# send_timeout 指定了发送给客户端应答后的超时时间
					elif re.search('send_timeout',line):
						send_timeout=clean_str(line)
						if not send_timeout[1]=="10":
							sorce=sorce-11
							results.append({'send_timeout':send_timeout[1]})
				obj_r.close()
			else:
				pass
		except:
			pass

	def save(self):
		if sorce<100:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-12","mod_name":"TnginxMod","status":"1","results":str(results)})
		else:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-12","mod_name":"TnginxMod","status":"0","results":"null"})
		print "[*] TnginxMod Finish!"

def getPluginClass():
	return TnginxMod
