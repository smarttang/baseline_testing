#coding:utf-8
from xml.dom import minidom,Node
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class ReportAnaly:
	global htmltext
	htmltext='''<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>基线检查报告</title></head><body><table border="1"><tr><td>检查编号</td><td>检查项目</td><td>检查结果</td><td>详细内容</td><td>解决方案</td></tr>'''
	def __init__(self,doc,output_name):
		self.output_name=output_name
		results=[]
		for child in doc.childNodes:
			if child.nodeType == Node.ELEMENT_NODE \
			and child.tagName == "module":
				mod_id = child.getAttribute("mod_id")
				for chil in child.childNodes:
					if chil.nodeType == Node.ELEMENT_NODE:
						if chil.tagName=="mod_name":
							mod_name=self.getText(chil.firstChild)
						if chil.tagName=="status_code":
							if self.getText(chil.firstChild).strip("\n\t")=="0":
								status_code="无风险"
							else:
								status_code="存在风险"
						if chil.tagName=="mod_results":
							if self.getText(chil.firstChild).strip("\n\t")=="null":
								mod_results="一切正常"
							else:
								mod_results=self.getText(chil.firstChild)
				if mod_id=="37wan-centOS-09":
					descp="(1)修改文件/etc/rc.d/rc.local，注释含有类似'echo ……>> /etc/issue' 信息的行，在行首添加'#'（2）删除/etc/issue、/etc/issue.net文件 mv /etc/issue /etc/issue.bak mv /etc/issue.net /etc/issue.net.bak"
				elif mod_id=="37wan-centOS-08":
					descp="(1)不要使用匿名ftp，修改vsftpd.conf文件，配置如下：anonymous_enable=NO (2)在文件/etc/vsftpd/ftpusers中增加超级用户 (3)打开/etc/vsftpd/chroot_list文件，将违规的用户名加入到文件中。"
				elif mod_id=="37wan-centOS-06":
					descp="修改文件权限，全部设置成640权限。命令：chmod 640 文件名。"
				elif mod_id=="37wan-centOS-04":
					descp="修改目录的权限设置，/etc/passwd 要求是644的权限。/etc/shadow 要求是400的权限。/etc/group 要求是644的权限。"
				elif mod_id=="37wan-centOS-07":
					descp="设置定时账户自动登出时间,修改/etc/profile文件，设置如下内容：export TMOUT=180;export TMOUT"
				elif mod_id=="37wan-centOS-03":
					descp="(1)设置密码生存周期修改文件/etc/login.defs，配置如下内容：PASS_MAX_DAYS=90。(2)设置默认权限,修改文件/etc/login.defs,配置'UMASK 027'。"
				elif mod_id=="37wan-centOS-10":
					descp="这些属于一些敏感的文件，解决办法就是删除这类文件。"
				elif mod_id=="37wan-centOS-02":
					descp="修改权限：chmod 750 directory  #其中750为设置的权限，可根据实际情况设置相应的权限，directory是要更改权限的目录或文件"
				elif mod_id=="37wan-centOS-05":
					descp="编辑/etc/passwd，帐号信息的shell 为/sbin/nologin 的为禁止远程登录，如要允许，则改成可以登录的shell 即可，如/bin/bash."
				elif mod_id=="37wan-centOS-01":
					descp="将这些无关的账号进行锁定,或者直接删除。"
				elif mod_id=="37wan-centOS-11":
					descp="开放的端口情况，具体信息。请根据实际业务需要来进行处理，哪些需要屏蔽请自行判断。"
				elif mod_id=="37wan-centOS-12":
					descp="标准的配置应该是如下:1、测试缓冲区溢出配置client_body_buffer_size  1K;client_header_buffer_size 1k;client_max_body_size 1k;large_client_header_buffers 2 1k;2、测试控制超时配置client_body_timeout   10;client_header_timeout 10;keepalive_timeout     5 5;send_timeout          10;"
				elif mod_id=="37wan-centOS-13":
					descp="标准的配置应该是如下:disable_functions=phpinfo, system, mail, exec  max_execution_time=30  max_input_time=60  memory_limit=8M  post_max_size=8M  file_uploads=Off  upload_max_filesize=2M  display_errors=Off  safe_mode=On  safe_mode_exec_dir=php-required-executables-path  safe_mode_allowed_env_vars=PHP_  expose_php=Off  log_errors=On  register_globals=Off  cgi.force_redirect=0  sql.safe_mode=On  allow_url_fopen=Off"
				elif mod_id=="37wan-centOS-14":
					descp="back_log = 300 max_connections = 3000 max_connect_errors = 30 table_cache = 4096 max_allowed_packet = 32M binlog_cache_size = 4M max_heap_table_size = 128M sort_buffer_size = 16M join_buffer_size = 16M thread_cache_size = 16 thread_concurrency = 8 query_cache_size = 128M query_cache_limit = 4M ft_min_word_len = 8 default_table_type = MYISAM thread_stack = 512K transaction_isolation = REPEATABLE-READ tmp_table_size = 128M log-bin=mysql-bin long_query_time = 6 server-id = 1 key_buffer_size = 128M read_buffer_size = 8M read_rnd_buffer_size = 64M bulk_insert_buffer_size = 256M myisam_sort_buffer_size = 256M myisam_max_sort_file_size = 10G myisam_max_extra_sort_file_size = 10G myisam_repair_threads = 1 innodb_additional_mem_pool_size = 64M innodb_buffer_pool_size = 6G innodb_data_file_path = ibdata1:10M:autoextend innodb_file_io_threads = 4 innodb_thread_concurrency = 16 innodb_flush_log_at_trx_commit = 2 innodb_log_buffer_size = 16M innodb_log_file_size = 512M innodb_log_files_in_group = 3 innodb_max_dirty_pages_pct = 90 innodb_lock_wait_timeout = 120 max_allowed_packet = 32M key_buffer = 2048M sort_buffer_size = 2048M read_buffer = 32M write_buffer = 32M open-files-limit = 8192"

				results.append("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>" % (mod_id.strip("\n\t"),mod_name.strip("\n\t"),status_code.strip("\n\t"),mod_results.strip("\n\t"),descp))
		content="".join(results)
		self.save_html(htmltext+content+"</table></body></html>")

	def getText(self,node):
		if node.nodeType == Node.TEXT_NODE:
			return node.nodeValue
		else:
			return ""

	def save_html(self,html):
		obj=open(self.output_name,"w")
		obj.write(html)
		obj.close()