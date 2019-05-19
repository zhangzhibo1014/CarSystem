#!/user/bin/python
# -*- coding:utf-8 -*-

from .db_utils import MysqlDB
import datetime
import logging

class DatabaseHandler(logging.Handler):

	def __init__(self,db_host,db_user,db_pass,db):
		logging.Handler.__init__(self)
		self.conn = MysqlDB(host=db_host,user=db_user,password=db_pass,db=db)

	def getRemoteIP(self,param):
		res = str(param.__enter__()).split(',')[-2][9:-1]
		return res

	def build_table(self,db):
		sql = """CREATE TABLE log (
			id  INT  AUTO_INCREMENT PRIMARY KEY,
			level  CHAR(4),
			content  VARCHAR(64),
			ip  CHAR(16),
			time datetime)"""
		db.insert(sql)

	def insert2db(self,db,record):
		request = record.request
		level = record.levelname
		msg = record.getMessage()
		_ip = self.getRemoteIP(request)
		_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		sql = "INSERT INTO log (level,content,ip,time) VALUES ('%s','%s','%s','%s')"%(level,msg,_ip,_time)
		db.insert(sql)

	def emit(self,record):
		try:
			db = self.conn
			self.insert2db(db,record)
		except:
			try:
				self.build_table(db)
				self.insert2db(db,record)
			except:
				pass

	def close(self):
		self.conn.close()
