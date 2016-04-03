#! -*- coding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('../db.db')
print "Open database successfully"


conn.execute(""" CREATE TABLE  BAIDU_INS
 (ID INT PRIMARY KEY NOT NULL,
 COMPANY_NAME TEXT NOT NULL,
 PRODUCT_NAME TEXT NOT NULL,
 PRODUCT_TYPE TEXT NOT NULL,
 PRODUCT_DESC CHAR(100))""")

conn.commit()
conn.close()
