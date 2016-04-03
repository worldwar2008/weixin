#! -*- coding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('../db.db')
print "Open database successfully"

create_txt = ''' CREATE TABLE  BAIDU_INS
 (ID INT PRIMARY KEY NOT NULL,
 COMPANY_NAME TEXT NOT NULL,
 PRODUCT_NAME TEXT NOT NULL,
 PRODUCT_DESC CHAR(100))
 ;)'''
conn.execute(create_txt)
conn.commit()
conn.close()
