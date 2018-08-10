# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .conf import *
import pymysql

class IpspiderprojectPipeline(object):
    def process_item(self, item, spider):
        return item


class PyMysqlPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(host=host,
                                     port=int(port),
                                     user=user,
                                     password=str(password),
                                     db=db_name,
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()


    def __query(self, sql, param=None):

        try:
            if param is None:
                count = self.cursor.execute(sql)
            else:
                count = self.cursor.execute(sql, param)
            self.conn.commit()

        finally:
            self.conn.close()
        return count

    def insert(self, sql, param=None):
        return self.__query(sql, param)

    def process_item(self, item, spider):
        sql = "INSERT INTO ip (id, ip, port,addr,anon,type,sudu,con_time,time_online,validate_time) VALUES(%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
        parm = (item['ip']+'_'+item['port'],item['ip'],item['port'],
                item['addr'],item['anon'],item['type'],item['sudu'],
                item['con_time'], item['time_online'], item['validate_time'],
                )
        print(parm)
        self.insert(sql,parm)
        return item

# if __name__ == '__main__':
#     a = PyMysqlPipeline()
#     sql = "INSERT INTO ip (id, ip, port,addr,anon,type,sudu,con_time,time_online,validate_time) VALUES(%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
#     parm = ('118.190.95.3_5', '118.190.95.35', '9001', '高匿', '广西', 'HTTP', '49天', '18-08-10 14:21', '0.052秒', '0.01秒')
#     print(a.insert(sql,parm))