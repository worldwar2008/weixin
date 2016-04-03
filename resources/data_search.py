# -*- coding:utf-8 -*-
import sqlite3
def find_data(cop_name,product_name):

    conn = sqlite3.connect("../db.db")
    cursor = conn.execute("""select * from  main.BAIDU_INS where main.BAIDU_INS.COMPANY_NAME == %s AND main.BAIDU_INS.PRODUCT_NAME == %s limit 1"""%(cop_name,product_name))
    result = cursor.fetchall()
    if cursor.arraysize==1:
        print result
    else:
        print [("抱歉,没有检索到你所要查询的信息,在未来我们会更加努力的去完善产品信息")]
    conn.close()
    print  result

find_data(u"中国平安保险",u"a")