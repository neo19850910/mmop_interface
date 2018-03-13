#-*- coding:utf8 -*-

import cx_Oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
def query():
    host = '192.168.0.150'
    port = '1521'
    sid = 'ORCL'
    dsn = cx_Oracle.makedsn(host, port, sid)
    db = cx_Oracle.connect("mmop", "mmop", dsn)
    return db
def db_chk_count():
    sql =  '''
            select SUBS_NO,NAME from d_subs
           '''
    db = query()
    cr = db.cursor()
    cr.execute(sql)
    rs = cr.fetchall()
    db.close()
    return rs
if __name__ =='__main__':
    print db_chk_count()