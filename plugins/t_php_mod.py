#coding:utf-8
import re

###################################
#
#	测试PHP.ini配置安全
#
####################################

def clean_str(_line):
	res=[]
	for item in _line.split("="):
		res.append(item.strip())
	return res

class TphpMod:
	global results,socre
	results=[]
	socre=100
	def setBaseline_main(self,baseline_main):
		self.baseline_main=baseline_main

	def start(self):
		check_path='/etc/php.ini'
		print "[*] Checking TphpMod!!"
		try:
			if os.path.exists(check_path):
				obj_r=open(check_path,"r")
				for line in obj_r:
					# Disallow dangerous functions
					if re.search("disable_functions",line):
						disable_functions=clean_str(line)
						if not disable_functions[1]=="phpinfo, system, mail, exec":
							socre=socre-15
							results.append({'disable_functions':disable_functions[1]})

					# Maximum execution time of each script, in seconds
					elif re.search("max_execution_time",line):
						max_execution_time=clean_str(line)
						if not max_execution_time[1]=="30":
							socre=socre-5
							results.append({'max_execution_time':max_execution_time[1]})

					# Maximum amount of time each script may spend parsing request data
					elif re.search("max_input_time",line):
						max_input_time=clean_str(line)
						if not max_input_time[1]=="60":
							socre=socre-5
							results.append({'max_input_time':max_input_time[1]})

					# Maximum amount of memory a script may consume (8MB)
					elif re.search("memory_limit",line):
						memory_limit=clean_str(line)
						if not memory_limit[1]=="8M":
							socre=socre-5
							results.append({'memory_limit':memory_limit[1]})

					# Maximum size of POST data that PHP will accept.
					elif re.search("post_max_size",line):
						post_max_size=clean_str(line)
						if not post_max_size[1]=="8M":
							socre=socre-5
							results.append({'post_max_size':post_max_size[1]})

					# Whether to allow HTTP file uploads.
					elif re.search("file_uploads",line):
						file_uploads=clean_str(line)
						if not file_uploads[1]=="Off":
							socre=socre-5
							results.append({'file_uploads':file_uploads[1]})

					# Maximum allowed size for uploaded files.
					elif re.search("upload_max_filesize",line):
						upload_max_filesize=clean_str(line)
						if not upload_max_filesize[1]=="2M":
							socre=socre-5
							results.append({'upload_max_filesize':upload_max_filesize[1]})

					# Do not expose PHP error messages to external users
					elif re.search("display_errors",line):
						display_errors=clean_str(line)
						if not display_errors[1]=="Off":
							socre=socre-5
							results.append({'display_errors':display_errors[1]})

					# Turn on safe mode
					elif re.search("safe_mode",line):
						safe_mode=clean_str(line)
						if not safe_mode[1]=="On":
							socre=socre-5
							results.append({'safe_mode':safe_mode[1]})

					# Only allow access to executables in isolated directory
					elif re.search("safe_mode_exec_dir",line):
						safe_mode_exec_dir=clean_str(line)
						if not safe_mode_exec_dir[1]=="php-required-executables-path":
							socre=socre-5
							results.append({'safe_mode_exec_dir':safe_mode_exec_dir[1]})

					# Limit external access to PHP environment
					elif re.search("safe_mode_allowed_env_vars",line):
						safe_mode_allowed_env_vars=clean_str(line)
						if not safe_mode_allowed_env_vars[1]=="PHP_":
							socre=socre-5
							results.append({'safe_mode_allowed_env_vars':safe_mode_allowed_env_vars[1]})

					# Restrict PHP information leakage
					elif re.search("expose_php",line):
						expose_php=clean_str(line)
						if not expose_php[1]=="Off":
							socre=socre-5
							results.append({'expose_php':expose_php[1]})

					# Log all errors
					elif re.search("log_errors",line):
						log_errors=clean_str(line)
						if not log_errors[1]=="On":
							socre=socre-7
							results.append({'log_errors':log_errors[1]})

					# Do not register globals for input data
					elif re.search("register_globals",line):
						register_globals=clean_str(line)
						if not register_globals[1]=="Off":
							socre=socre-5
							results.append({'register_globals':register_globals[1]})

					# Ensure PHP redirects appropriately
					elif re.search("cgi.force_redirect",line):
						cgi_force_redirect=clean_str(line)
						if not cgi_force_redirect[1]=="0":
							socre=socre-5
							results.append({'cgi.force_redirect':cgi_force_redirect[1]})

					# Enable SQL safe mode
					elif re.search("sql.safe_mode",line):
						sql_safe_mode=clean_str(line)
						if not sql_safe_mode[1]=="On":
							socre=socre-8
							results.append({'sql.safe_mode':sql_safe_mode[1]})

					# Avoid Opening remote files
					elif re.search("allow_url_fopen",line):
						allow_url_fopen=clean_str(line)
						if not allow_url_fopen[1]=="Off":
							socre=socre-5
							results.append({'allow_url_fopen':allow_url_fopen[1]})
			else:
				pass
		except:
			pass

	def save(self):
		if socre<100:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-13","mod_name":"TphpMod","status":"1","results":str(results)})
		else:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-13","mod_name":"TphpMod","status":"0","results":"null"})
		print "[*] TphpMod Finish!"

def getPluginClass():
	return TphpMod