#coding:utf-8
import re
import os

###################################
#
#	Mysql配置测试模块
#	mysql 文件地址需要自己配置
#
####################################

def clean_str(_line):
	res=[]
	for item in _line.split("="):
		res.append(item.strip())
	return res

class TmysqlMod:
	global results,sorce
	results=[]
	sorce=400
	def setBaseline_main(self,baseline_main):
		self.baseline_main=baseline_main

	def start(self):
		mysql_path=['/xxx/xxxx/my1.cnf','/xxxx/xxxx/my.cnf','/xxxx/xxxx/xxxxx/my.cnf','/xxxxx/xxxxx/xxxxxx/my.cnf']
		print "[*] Checking T_mysql_Mod!!"
		try:
			for file_n in mysql_path:

				if os.path.exists(file_n):
					re_tmp={file_n:{}}
					obj_r=open(file_n,"r")
					for line in obj_r:
						
						# back_log 是操作系统在监听队列中所能保持的连接数,
						if re.search("back_log",line):
							back_log=clean_str(line)
							if not re.match("^#",back_log[0]):
								if not back_log[1]=="300":
									sorce=sorce-2
									re_tmp[file_n].update({'back_log':back_log[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'back_log':'Disable'})


						# MySQL 服务所允许的同时会话数的上限
						elif re.search("max_connections",line):
							max_connections=clean_str(line)
							if not re.match("^#",max_connections[0]):
								if not max_connections[1]=="3000":
									sorce=sorce-2
									re_tmp[file_n].update({'max_connections':max_connections[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'max_connections':'Disable'})

						# 每个客户端连接最大的错误允许数量,如果达到了此限制.
						elif re.search("max_connect_errors",line):
							max_connect_errors=clean_str(line)
							if not re.match("^#",max_connect_errors[0]):
								if not max_connect_errors[1]=="30":
									sorce=sorce-2
									re_tmp[file_n].update({'max_connect_errors':max_connect_errors[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'max_connect_errors':'Disable'})

						# 所有线程所打开表的数量.
						elif re.search("table_cache",line):
							table_cache=clean_str(line)
							if not re.match("^#",table_cache[0]):
								if not table_cache[1]=="4096":
									sorce=sorce-2
									re_tmp[file_n].update({'table_cache':table_cache[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'table_cache':'Disable'})

						# 每个连接独立的大小.大小动态增加
						elif re.search("max_allowed_packet",line):
							max_allowed_packet=clean_str(line)
							if not re.match("^#",max_allowed_packet[0]):
								if not max_allowed_packet[1]=="32M":
									sorce=sorce-2
									re_tmp[file_n].update({'max_allowed_packet':max_allowed_packet[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'max_allowed_packet':'Disable'})

						# 在一个事务中binlog为了记录SQL状态所持有的cache大小
						elif re.search("binlog_cache_size",line):
							binlog_cache_size=clean_str(line)
							if not re.match("^#",binlog_cache_size[0]):
								if not binlog_cache_size[1]=="4M":
									sorce=sorce-2
									re_tmp[file_n].update({'binlog_cache_size':binlog_cache_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'binlog_cache_size':'Disable'})

						# 独立的内存表所允许的最大容量.
						elif re.search("max_heap_table_size",line):
							max_heap_table_size=clean_str(line)
							if not re.match("^#",max_heap_table_size[0]):
								if not max_heap_table_size[1]=="128M":
									sorce=sorce-2
									re_tmp[file_n].update({'max_heap_table_size':max_heap_table_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'max_heap_table_size':'Disable'})

						# 排序缓冲被用来处理类似ORDER BY以及GROUP BY队列所引起的排序
						elif re.search("sort_buffer_size",line):
							sort_buffer_size=clean_str(line)
							if not re.match("^#",sort_buffer_size[0]):
								if not sort_buffer_size[1]=="16M":
									sorce=sorce-2
									re_tmp[file_n].update({'sort_buffer_size':sort_buffer_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'sort_buffer_size':'Disable'})

						# 此缓冲被使用来优化全联合(full JOINs 不带索引的联合).
						elif re.search("join_buffer_size",line):
							join_buffer_size=clean_str(line)
							if not re.match("^#",join_buffer_size[0]):
								if not join_buffer_size[1]=="16M":
									sorce=sorce-2
									re_tmp[file_n].update({'join_buffer_size':join_buffer_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'join_buffer_size':'Disable'})

						# 我们在cache中保留多少线程用于重用
						elif re.search("thread_cache_size",line):
							thread_cache_size=clean_str(line)
							if not re.match("^#",thread_cache_size[0]):
								if not thread_cache_size[1]=="16":
									sorce=sorce-2
									re_tmp[file_n].update({'thread_cache_size':thread_cache_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'thread_cache_size':'Disable'})

						# 此允许应用程序给予线程系统一个提示在同一时间给予渴望被运行的线程的数量.
						elif re.search("thread_concurrency",line):
							thread_concurrency=clean_str(line)
							if not re.match("^#",thread_concurrency[0]):
								if not thread_concurrency[1]=="8":
									sorce=sorce-2
									re_tmp[file_n].update({'thread_concurrency':thread_concurrency[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'thread_concurrency':'Disable'})

						# 查询缓冲常被用来缓冲 SELECT 的结果并且在下一次同样查询的时候不再执行直接返回结果.
						elif re.search("query_cache_size",line):
							query_cache_size=clean_str(line)
							if not re.match("^#",query_cache_size[0]):
								if not query_cache_size[1]=="128M":
									sorce=sorce-2
									re_tmp[file_n].update({'query_cache_size':query_cache_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'query_cache_size':'Disable'})

						# 此设置用来保护查询缓冲,防止一个极大的结果集将其他所有的查询结果都覆盖.
						elif re.search("query_cache_limit",line):
							query_cache_limit=clean_str(line)
							if not re.match("^#",query_cache_limit[0]):
								if not query_cache_limit[1]=="4M":
									sorce=sorce-2
									re_tmp[file_n].update({'query_cache_limit':query_cache_limit[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'query_cache_limit':'Disable'})

						# 被全文检索索引的最小的字长.
						elif re.search("ft_min_word_len",line):
							ft_min_word_len=clean_str(line)
							if not re.match("^#",ft_min_word_len[0]):
								if not ft_min_word_len[1]=="8":
									sorce=sorce-2
									re_tmp[file_n].update({'ft_min_word_len':ft_min_word_len[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'ft_min_word_len':'Disable'})

						# 当创建新表时作为默认使用的表类型,
						elif re.search("default_table_type",line):
							default_table_type=clean_str(line)
							if not re.match("^#",default_table_type[0]):
								if not default_table_type[1]=="MYISAM":
									sorce=sorce-2
									re_tmp[file_n].update({'default_table_type':default_table_type[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'default_table_type':'Disable'})

						# 线程使用的堆大小. 此容量的内存在每次连接时被预留.
						elif re.search("thread_stack",line):
							thread_stack=clean_str(line)
							if not re.match("^#",thread_stack[0]):
								if not thread_stack[1]=="512K":
									sorce=sorce-2
									re_tmp[file_n].update({'thread_stack':thread_stack[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'thread_stack':'Disable'})

						# 设定默认的事务隔离级别.可用的级别如下
						elif re.search("transaction_isolation",line):
							transaction_isolation=clean_str(line)
							if not re.match("^#",transaction_isolation[0]):
								if not transaction_isolation[1]=="REPEATABLE-READ":
									sorce=sorce-2
									re_tmp[file_n].update({'transaction_isolation':transaction_isolation[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'transaction_isolation':'Disable'})

						# 此限制是针对单个表的,而不是总和.
						elif re.search("tmp_table_size",line):
							tmp_table_size=clean_str(line)
							if not re.match("^#",tmp_table_size[0]):
								if not tmp_table_size[1]=="128M":
									sorce=sorce-2
									re_tmp[file_n].update({'tmp_table_size':tmp_table_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'tmp_table_size':'Disable'})

						# 如果你需要从你最后的备份中做基于时间点的恢复,你也同样需要二进制日志.
						elif re.search("log-bin",line):
							log_bin=clean_str(line)
							if not re.match("^#",log_bin[0]):
								if not log_bin[1]=="mysql-bin":
									sorce=sorce-2
									re_tmp[file_n].update({'log-bin':log_bin[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'log-bin':'Disable'})

						# 所有的使用了比这个时间(以秒为单位)更多的查询会被认为是慢速查询.
						elif re.search("long_query_time",line):
							long_query_time=clean_str(line)
							if not re.match("^#",long_query_time[0]):
								if not long_query_time[1]=="6":
									sorce=sorce-2
									re_tmp[file_n].update({'long_query_time':long_query_time[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'long_query_time':'Disable'})

						# 如果 “master-host” 没有被设置,则默认为1, 但是如果忽略此选项,MySQL不会作为master生效.
						elif re.search("server-id",line):
							server_id=clean_str(line)
							if not re.match("^#",server_id[0]):
								if not server_id[1]=="1":
									sorce=sorce-2
									re_tmp[file_n].update({'server-id':server_id[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'server-id':'Disable'})

						# 关键词缓冲的大小, 一般用来缓冲MyISAM表的索引块.
						elif re.search("key_buffer_size",line):
							key_buffer_size=clean_str(line)
							if not re.match("^#",key_buffer_size[0]):
								if not key_buffer_size[1]=="128M":
									sorce=sorce-2
									re_tmp[file_n].update({'key_buffer_size':key_buffer_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'key_buffer_size':'Disable'})

						# 用来做MyISAM表全表扫描的缓冲大小.
						elif re.search("read_buffer_size",line):
							read_buffer_size=clean_str(line)
							if not re.match("^#",read_buffer_size[0]):
								if not read_buffer_size[1]=="8M":
									sorce=sorce-2
									re_tmp[file_n].update({'read_buffer_size':read_buffer_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'read_buffer_size':'Disable'})

						# 当在排序之后,从一个已经排序好的序列中读取行时,行数据将从这个缓冲中读取来防止磁盘寻道.
						elif re.search("read_rnd_buffer_size",line):
							read_rnd_buffer_size=clean_str(line)
							if not re.match("^#",read_rnd_buffer_size[0]):
								if not read_buffer_size[1]=="64M":
									sorce=sorce-2
									re_tmp[file_n].update({'read_rnd_buffer_size':read_rnd_buffer_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'read_rnd_buffer_size':'Disable'})

						# 当突发插入被检测到时此缓冲将被分配.
						elif re.search("bulk_insert_buffer_size",line):
							bulk_insert_buffer_size=clean_str(line)
							if not re.match("^#",bulk_insert_buffer_size[0]):
								if not bulk_insert_buffer_size[1]=="256M":
									sorce=sorce-2
									re_tmp[file_n].update({'bulk_insert_buffer_size':bulk_insert_buffer_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'bulk_insert_buffer_size':'Disable'})

						# 此缓冲当MySQL需要在 REPAIR, OPTIMIZE, ALTER 以及 LOAD DATA INFILE 到一个空表中引起重建索引时被分配.
						elif re.search("myisam_sort_buffer_size",line):
							myisam_sort_buffer_size=clean_str(line)
							if not re.match("^#",myisam_sort_buffer_size[0]):
								if not myisam_sort_buffer_size[1]=="256M":
									sorce=sorce-2
									re_tmp[file_n].update({'myisam_sort_buffer_size':myisam_sort_buffer_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'myisam_sort_buffer_size':'Disable'})

						# MySQL重建索引时所允许的最大临时文件的大小 (当 REPAIR, ALTER TABLE 或者 LOAD DATA INFILE).
						elif re.search("myisam_max_sort_file_size",line):
							myisam_max_sort_file_size=clean_str(line)
							if not re.match("^#",myisam_max_sort_file_size[0]):
								if not myisam_max_sort_file_size[1]=="10G":
									sorce=sorce-2
									re_tmp[file_n].update({'myisam_max_sort_file_size':myisam_max_sort_file_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'myisam_max_sort_file_size':'Disable'})

						# 如果被用来更快的索引创建索引所使用临时文件大于制定的值,那就使用键值缓冲方法.
						elif re.search("myisam_max_extra_sort_file_size",line):
							myisam_max_extra_sort_file_size=clean_str(line)
							if not re.match("^#",myisam_max_extra_sort_file_size[0]):
								if not myisam_max_extra_sort_file_size[1]=="10G":
									sorce=sorce-2
									re_tmp[file_n].update({'myisam_max_extra_sort_file_size':myisam_max_extra_sort_file_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'myisam_max_extra_sort_file_size':'Disable'})

						# 如果被用来更快的索引创建索引所使用临时文件大于制定的值,那就使用键值缓冲方法.
						elif re.search("myisam_repair_threads",line):
							myisam_repair_threads=clean_str(line)
							if not re.match("^#",myisam_repair_threads[0]):
								if not myisam_repair_threads[1]=="1":
									sorce=sorce-2
									re_tmp[file_n].update({'myisam_repair_threads':myisam_repair_threads[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'myisam_repair_threads':'Disable'})

						# 附加的内存池被InnoDB用来保存 metadata 信息
						elif re.search("innodb_additional_mem_pool_size",line):
							innodb_additional_mem_pool_size=clean_str(line)
							if not re.match("^#",innodb_additional_mem_pool_size[0]):
								if not innodb_additional_mem_pool_size[1]=="64M":
									sorce=sorce-2
									re_tmp[file_n].update({'innodb_additional_mem_pool_size':innodb_additional_mem_pool_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'innodb_additional_mem_pool_size':'Disable'})

						# InnoDB使用一个缓冲池来保存索引和原始数据, 不像 MyISAM.
						elif re.search("innodb_buffer_pool_size",line):
							innodb_buffer_pool_size=clean_str(line)
							if not re.match("^#",innodb_buffer_pool_size[0]):
								if not innodb_buffer_pool_size[1]=="6G":
									sorce=sorce-2
									re_tmp[file_n].update({'innodb_buffer_pool_size':innodb_buffer_pool_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'innodb_buffer_pool_size':'Disable'})

						# InnoDB 将数据保存在一个或者多个数据文件中成为表空间.
						elif re.search("innodb_data_file_path",line):
							innodb_data_file_path=clean_str(line)
							if not re.match("^#",innodb_data_file_path[0]):
								if not innodb_data_file_path[1]=="ibdata1:10M:autoextend":
									sorce=sorce-2
									re_tmp[file_n].update({'innodb_data_file_path':innodb_data_file_path[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'innodb_data_file_path':'Disable'})

						# 用来同步IO操作的IO线程的数量. 
						elif re.search("innodb_file_io_threads",line):
							innodb_file_io_threads=clean_str(line)
							if not re.match("^#",innodb_file_io_threads[0]):
								if not innodb_file_io_threads[1]=="4":
									sorce=sorce-2
									re_tmp[file_n].update({'innodb_file_io_threads':innodb_file_io_threads[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'innodb_file_io_threads':'Disable'})

						# 在InnoDb核心内的允许线程数量.
						elif re.search("innodb_thread_concurrency",line):
							innodb_thread_concurrency=clean_str(line)
							if not re.match("^#",innodb_thread_concurrency[0]):
								if not innodb_thread_concurrency[1]=="16":
									sorce=sorce-2
									re_tmp[file_n].update({'innodb_thread_concurrency':innodb_thread_concurrency[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'innodb_thread_concurrency':'Disable'})

						# 如果设置为1 ,InnoDB会在每次提交后刷新(fsync)事务日志到磁盘上,
						elif re.search("innodb_flush_log_at_trx_commit",line):
							innodb_flush_log_at_trx_commit=clean_str(line)
							if not re.match("^#",innodb_flush_log_at_trx_commit[0]):
								if not innodb_flush_log_at_trx_commit[1]=="2":
									sorce=sorce-2
									re_tmp[file_n].update({'innodb_flush_log_at_trx_commit':innodb_flush_log_at_trx_commit[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'innodb_flush_log_at_trx_commit':'Disable'})

						# 用来缓冲日志数据的缓冲区的大小.
						elif re.search("innodb_log_buffer_size",line):
							innodb_log_buffer_size=clean_str(line)
							if not re.match("^#",innodb_log_buffer_size[0]):
								if not innodb_log_buffer_size[1]=="16M":
									sorce=sorce-2
									re_tmp[file_n].update({'innodb_log_buffer_size':innodb_log_buffer_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'innodb_log_buffer_size':'Disable'})

						# 在日志组中每个日志文件的大小
						elif re.search("innodb_log_file_size",line):
							innodb_log_file_size=clean_str(line)
							if not re.match("^#",innodb_log_file_size[0]):
								if not innodb_log_file_size[1]=="512M":
									sorce=sorce-2
									re_tmp[file_n].update({'innodb_log_file_size':innodb_log_file_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'innodb_log_file_size':'Disable'})

						# 在日志组中的文件总数
						elif re.search("innodb_log_files_in_group",line):
							innodb_log_files_in_group=clean_str(line)
							if not re.match("^#",innodb_log_files_in_group[0]):
								if not innodb_log_files_in_group[1]=="3":
									sorce=sorce-2
									re_tmp[file_n].update({'innodb_log_files_in_group':innodb_log_files_in_group[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'innodb_log_files_in_group':'Disable'})

						# 在InnoDB缓冲池中最大允许的脏页面的比例.
						elif re.search("innodb_max_dirty_pages_pct",line):
							innodb_max_dirty_pages_pct=clean_str(line)
							if not re.match("^#",innodb_max_dirty_pages_pct[0]):
								if not innodb_max_dirty_pages_pct[1]=="90":
									sorce=sorce-2
									re_tmp[file_n].update({'innodb_max_dirty_pages_pct':innodb_max_dirty_pages_pct[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'innodb_max_dirty_pages_pct':'Disable'})

						# 在被回滚前,一个InnoDB的事务应该等待一个锁被批准多久.
						elif re.search("innodb_lock_wait_timeout",line):
							innodb_lock_wait_timeout=clean_str(line)
							if not re.match("^#",innodb_lock_wait_timeout[0]):
								if not innodb_lock_wait_timeout[1]=="120":
									sorce=sorce-2
									re_tmp[file_n].update({'innodb_lock_wait_timeout':innodb_lock_wait_timeout[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'innodb_lock_wait_timeout':'Disable'})

						###############################################
						#
						#	将结果导出时的缓存设置安全
						#
						###############################################
						elif re.search("max_allowed_packet",line):
							max_allowed_packet=clean_str(line)
							if not re.match("^#",max_allowed_packet[0]):
								if not max_allowed_packet[1]=="32M":
									sorce=sorce-2
									re_tmp[file_n].update({'max_allowed_packet':max_allowed_packet[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'max_allowed_packet':'Disable'})

						elif re.search("key_buffer",line):
							key_buffer=clean_str(line)
							if not re.match("^#",key_buffer[0]):
								if not key_buffer[1]=="2048M":
									sorce=sorce-2
									re_tmp[file_n].update({'key_buffer':key_buffer[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'key_buffer':'Disable'})

						elif re.search("sort_buffer_size",line):
							sort_buffer_size=clean_str(line)
							if not re.match("^#",sort_buffer_size[0]):
								if not sort_buffer_size[1]=="2048M":
									sorce=sorce-2
									re_tmp[file_n].update({'sort_buffer_size':sort_buffer_size[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'sort_buffer_size':'Disable'})

						elif re.search("read_buffer",line):
							read_buffer=clean_str(line)
							if not re.match("^#",read_buffer[0]):
								if not read_buffer[1]=="32M":
									sorce=sorce-2
									re_tmp[file_n].update({'read_buffer':read_buffer[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'read_buffer':'Disable'})

						elif re.search("write_buffer",line):
							write_buffer=clean_str(line)
							if not re.match("^#",write_buffer[0]):
								if not write_buffer[1]=="32M":
									sorce=sorce-2
									re_tmp[file_n].update({'write_buffer':write_buffer[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'write_buffer':'Disable'})

						elif re.search("open-files-limit",line):
							open_files_limit=clean_str(line)
							if not re.match("^#",open_files_limit[0]):
								if not open_files_limit[1]=="8192":
									sorce=sorce-2
									re_tmp[file_n].update({'open-files-limit':open_files_limit[1]})
							else:
								sorce=sorce-2
								re_tmp[file_n].update({'open-files-limit':'Disable'})
					results.append(re_tmp)
				else:
					print "[*] Mysql Path: %s No Found My.cnf" % file_n

		except:
			pass

	def save(self):
		if sorce<400:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-14","mod_name":"TmysqlMod","status":"1","results":str(results)})
		else:
			self.baseline_main.xml_result({"mod_id":"37wan-centOS-14","mod_name":"TmysqlMod","status":"0","results":"null"})
		print "[*] T_mysql_Mod Finish!"

def getPluginClass():
	return TmysqlMod