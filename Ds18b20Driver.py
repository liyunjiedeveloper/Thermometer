#DS18B20 28-0315a6095cff

class Ds18b20Driver():
    def __init__(self, name):
        self.name = name

    def getCurrentTemperature(self):
        tf = open("/sys/bus/w1/devices/%s/w1_slave" % (self.name), "r")
        text = tf.read()
        tf.close()
        temp = text.split()[-1].split("=")[-1]
        return "%s" % (float(temp) / 1000)
