# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .conf import *
import pymysql
num = 1
class IpspiderprojectPipeline(object):
    def __init__(self):
        self.ft = open('ip.json','a')

    def process_item(self, item, spider):
        self.ft.write(str(dict(item)) + '\n')
        global num
        print('已经写入%s条' % str(num))
        num +=1
        return item
    def __del__(self):
        self.ft.close()


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

    def insert(self, sql, param=None):
        count = self.cursor.execute(sql, param)
        self.conn.commit()
        return count

    def process_item(self, item, spider):
        sql = "INSERT INTO ip (id, ip, port,addr,anon,type,sudu,con_time,time_online,validate_time) VALUES(%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
        parm = (item['ip']+'_'+item['port'],item['ip'],item['port'],
                item['addr'],item['anon'],item['type'],item['sudu'],
                item['con_time'], item['time_online'], item['validate_time'],
                )
        print(parm)
        self.insert(sql,parm)
        return item

    # def __del__(self):
    #     self.conn.close()