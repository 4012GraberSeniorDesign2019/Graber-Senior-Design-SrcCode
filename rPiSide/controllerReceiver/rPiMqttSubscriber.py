#Receiver Side 
import paho.mqtt.client as mqtt
import time
import serial
import pdb

<<<<<<< HEAD:rPiSide/rPiMqttSubscriber.py
broker = "143.215.102.14" #Always set this to the IP addr of the PC 
=======
broker = "143.215.102.14" #Change to the IP addr of the PC every reconnect
>>>>>>> e5c336fba68ae02db86889b16099b31e0152e75c:rPiSide/controllerReceiver/rPiMqttSubscriber.py
port = 1883
topic = "test"

tempMsg = ''

def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))

    client.subscribe(broker)

def on_message(client, userdata, msg):


    print(msg.topic +" "+str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker,port)
client.subscribe(topic)
client.on_message

client.loop_forever()
