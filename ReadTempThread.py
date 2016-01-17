import threading
import time
from TemperatureDataBase import TempDB
from Ds18b20Driver import Ds18b20Driver

class ReadTempThread(threading.Thread):
    def __init__(self, num, interval):
        threading.Thread.__init__(self)
        self.num = num
        self.interval = interval
        self.stop = False
        self.ds18 = Ds18b20Driver("28-0315a6095cff")

    def run(self):
        self.db = TempDB(self.getDbName())
        self.db.open()
        while not self.stop:
            self.db.insertData(self.getTime(), self.ds18.getCurrentTemperature())
            time.sleep(self.interval)
        self.db.close()

    def stop(self):
        self.stop = True

    def getDbName(self):
        tm = time.localtime(time.time())
        return "%04d-%02d-%02d" % (tm[0], tm[1], tm[2])

    def getTime(self):
        tm = time.localtime(time.time())
        return "%02d:%02d:%02d" % (tm[3], tm[4], tm[5])