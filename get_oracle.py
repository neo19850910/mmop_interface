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

def db_chking():
    sql = '''
               SELECT DISTINCT T.SUBS_NO AS SUBS
      FROM T_TEST_PLAN P, T_TEST_PLAN_DET T, T_SITECHK_ORDER U
     WHERE P.PLAN_NO = T.PLAN_NO
       AND U.PLAN_NO = P.PLAN_NO
       AND P.CYCLE_CODE <> '01'
       AND TO_CHAR(P.WORK_S_DATE, 'yyyymm') = TO_CHAR(SYSDATE, 'yyyymm')
              '''
    db = query()
    cr = db.cursor()
    cr.execute(sql)
    rs = cr.fetchall()
    db.close()
    return rs
