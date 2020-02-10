from datetime import datetime
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def get_time():
    return datetime.now().strftime("%Y-%m-%d-%H")

def get_temp():
    _, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return temp

#line = get_time() + ";" + str(get_temp()) + "\n"
line = "%s;%.2f\n" % (get_time(), get_temp())

file = open("temp-log.csv", "a")
file.write(line)
file.close()
