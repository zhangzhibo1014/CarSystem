#!/usr/bin/python
# -*- coding:utf-8 -*-

import pymysql as ps

class MysqlDB(object):

	def __init__(self,host,user,password,db):
		self.conn = ps.connect(host=host,user=user,password=password,db=db,charset='UTF8')
		self.cursor = self.conn.cursor()

	def getItemsByParam(self,sql,param):
		rows = self.cursor.execute(sql%param)
		if rows != 0:
			res = self.cursor.fetchall()
			return res
		return None

	def getOneByParam(self,sql,param):
		row = self.cursor.execute(sql%param)
		if row != 0:
			res = self.cursor.fetchone()
			return res
		return None

	def getByParams(self,sql,params):
		in_p=', '.join(list(map(lambda x:'%s',params)))
		sql = sql%in_p
		row = self.cursor.execute(sql,params)
		if row != 0:
			res = list(self.cursor.fetchall())
			return res
		return None

	def insert(self,sql):
		self.cursor.execute(sql)
		self.conn.commit()

	def close(self):
		self.cursor.close()
		self.conn.close()
