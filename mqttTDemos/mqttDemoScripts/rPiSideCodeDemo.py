import clientObjClass as cli
import guiPublisher as guiPub
import controlSubscriber as controlSub
import pdb
import time
import serial
import random
from multiprocessing import Process 

guiBroker = '143.215.101.233' #Always change this to the ip address sending the info
controlBroker = '143.215.106.226' #IP address of the device the controller is connected to
port = 1883 #Port for MQTT info
videoPort = 8000 #Port for video streaming
topic1 = 'guiParseTest' #topic for Gui Data
topic2 = 'controllerTest' #topic for controller data
tracker = 0
#sensorData = ''
resolution = (640,480)
framerate = 100
baudrate = 9600
timeout = 2

Loop = True

cliePub = guiPub.guiPublisher()
clieSub = controlSub.controlSubscriber()


def initialize():
    print("start init")
    #Initializing
    cliePub.buildPublisher()
    clieSub.buildSubscriber()
    cliePub.addPublisherParams(guiBroker,port,topic1)
    clieSub.addSubscriberParams(controlBroker,port,topic2)
    clieSub.setSerialPort("/dev/ttyACM0")
    cliePub.buildSocket()
    pubClient = cliePub.getClient()
    controlSubClient = clieSub.getClient()
    #Connecting the publishers and subscribers
    cliePub.connectPublisher()
    clieSub.connectSubscriber()
    print("connected")
    #Connect to Arduino DUE
    clieSub.connectToDUE()
    #Connect publisher to serial port
    status = cliePub.connectSerialPort(baudrate,timeout)

    #Checking details of the client
    a = clieSub.checkConnection()
    b = clieSub.checkClientDetails()
    c = cliePub.checkClientDetails()
    d = cliePub.checkConnection()

    print("Subscriber details")
    print(a)
    print("Subscriber is connected: ")
    print(b)
    print("Publisher details")
    print(c)
    print("Publisher is connected: ")
    print(d)
    pubClient = cliePub.getClient()
    controlSubClient = clieSub.getClient()
    print(pubClient)
    print(controlSubClient)

    print(status)
    print("done")


#All the MQTT protocols packaged into one function to be threaded
def threadedMQTTProtocols():
    while Loop == True:
        mvmntData = clieSub.receiveMvmnt()
        sensorData = clieSub.writeToDUE(mvmntData)
        g = cliePub.publishInfo(sensorData)

def threadedVideoProtocols(res = resolution, fr = framerate):
    #Connect socket for streaming
    cliePub.connectSocket(controlBroker,videoPort)
    print("video connected")
    cliePub.startStream(res,fr)


def main():
    #while True:
        #try:
    initialize()
        #except:
            #print("initialize failed, trying again")
    #while True:
    #videoProcess = Process(target = threadedVideoProtocols)
    #mqttProcess = Process(target = threadedMQTTProtocols)
    print("process")
    try:
        #try:
        #mqttProcess.start()
        #videoProcess.start()
        threadedMQTTProtocols()    
        #mqttProcess.join()
        #videoProcess.join()
        #except:
        #Loop = False
        #print("issue")
    finally:
        #mqttProcess.terminate()
        #videoProcess.terminate()
        print("terminated")
        #initialize()

if __name__ == '__main__':
    main()
