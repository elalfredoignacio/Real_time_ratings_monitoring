from os import listdir
from os.path import isfile, join
import threading, time
import requests
import paho.mqtt.client as mqtt
import json

MODO = "mqtt"


class Amazon(threading.Thread):

    def __init__(self, amazon,  time, data, mode = ""):
        super(Amazon, self).__init__()
        self.amazon = amazon
        self.time = time
        self.data = data
        self.mode = mode

        if mode == 'mqtt':
            self.client = mqtt.Client()
            self.client.connect("127.0.0.1", 1883, 60)

    def run(self):
        for entry in self.data:
            if entry != "-":
                if self.mode == "rest":
                    self.enviar_request_response(entry)
                elif self.mode == "mqtt":
                    self.enviar_mqtt(entry)
                else:
                    print("[{0}] {1}".format(self.amazon, entry))

            time.sleep(self.time)

        print("[{0}] Fin de simulacion".format(self.amazon))

    
    def enviar_request_response(self, entry):
        parts = entry.split(",")
        data = {
	    "reviewerID": str(parts[0]),
            "productID": str(parts[1]),
            "rating": int(parts[2]),
            "timestamp": int(parts[3]),
	    "dummy": "a"	            

        }

        response = requests.post("http://localhost:5000/amazon", data)
        if response.status_code == 200:
            print("{0} envio datos".format(self.amazon))
        else:
            print("{0} no pudo enviar datos".format(self.amazon))
       

    def enviar_mqtt(self, entry):
        parts = entry.split(",")
        data = json.dumps({
	    "reviewerID": str(parts[0]),
            "productID": str(parts[1]),
            "rating": int(parts[2]),
            "timestamp": int(parts[3]),
	    "dummy": "a"            
        })

        self.client.publish("amazon", payload=data, qos=0, retain=False)



print("Cargando datos ...")

mypath = "./simulacion"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

ratings = {}
for path in onlyfiles:
    amazon = path.split('/')[-1].replace('.txt', '')

    ratings[amazon] = []

    with open("./simulacion/{0}".format(path)) as archivo:
        for linea in archivo:
            linea = linea.replace('\r','').replace('\n','')
            if len(linea)>0:
                ratings[amazon].append(linea)

print("Iniciando simulacion para ratings amazon".format(len(ratings)))

intervalo = int(input("intervalo (segs.)? "))
for amazon, valores in ratings.items():
    c = Amazon(amazon, intervalo, valores, MODO)
    c.start()
    time.sleep(1)
