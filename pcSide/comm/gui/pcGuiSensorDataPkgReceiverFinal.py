#Communication protocol (subscriber end) for the Raspberry Pi to the PC to
#send GUI info

import paho.mqtt.client as mqtt
import time
import serial
import pdb

class guiSensorDataReceiver(object):
    """Class accepting the sensor inputs from the rPi and translating it into lists"""

    broker = "143.215.98.187" #Always set this to the IP addr of the RPi
    port = 1883
    global topic
    topic = "guiSensorData"
    global client
    client = mqtt.Client()
    on_connect = client.on_connect
    on_message = client.on_message
    #client.connect(broker,port)
    client.subscribe(topic)
    client.on_message
    sensorData = {'Air Quality': 0.0, 'Infrared Temp Sensor': 0.0, 'Gas Content Sensor': 0.0}

    def on_connect(client, userdata, rc):
        print("Connected with result code "+str(rc))

        client.subscribe(broker)

    def on_message(client, userdata, msg):
        print(msg.topic +" "+str(msg.payload))

    def dataPkg()
        sensorData['AirQuality']
        sensorData['IR Temp']
        sensorData['Gas Content']



if __name__ == "__main__":
    guiData = guiSensorDataReceiver()
    guiData.init()
    guiData.dataPkg() #Assigns events to dictionaries
