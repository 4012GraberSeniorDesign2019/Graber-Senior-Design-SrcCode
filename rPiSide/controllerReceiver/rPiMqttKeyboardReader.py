import paho.mqtt.client as mqtt
import time
import serial
import pdb

broker = "143.215.102.14"
port = 1883
topic = "test"

tempMsg = ''

def on_connect(client, userdata, rc):
        print("Connected with result code "+str(rc))

        client.subscribe(broker)

def on_message(client, userdata, msg):


        #print(msg.topic +" "+str(msg.payload))
	output = str(msg.payload)

        if("pressed" in output):
            print("button pushed!")
	else:
	    print("button released!")

        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker,port)
client.subscribe(topic)
client.on_message


client.loop_forever()

