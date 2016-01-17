#创建每天的数据库存储测量温度

import time
import sqlite3
import os


class TempDB():
    def __init__(self, dbName):
            self.dbName = dbName

    def open(self):
        if self.fileIsExist():
            self.db = sqlite3.connect(self.dbName)
        else:
            self.db = sqlite3.connect(self.dbName)
            self.createTables()


    def currentTime(self):
        lt = time.localtime(time.time())
        return "%04d-%02d-%02d" % (lt[0], lt[1], lt[2])

    def fileIsExist(self):
        return os.path.exists(self.dbName)

    def createTables(self):
        self.db.execute("""
        CREATE TABLE TemperatureOfDay
        (time VARCHAR(20),
        temperature VARCHAR(10));
        """)

    def insertData(self, time, temp):
        sql = "insert into TemperatureOfDay (time, temperature) values ('%s', '%s')" % (time, temp)
        self.db.execute(sql)
        self.db.commit()

    def close(self):
        self.db.close()