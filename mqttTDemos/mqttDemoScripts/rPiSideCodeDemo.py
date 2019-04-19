import clientObjClass as cli
import guiPublisher as guiPub
import controlSubscriber as controlSub
import pdb
import time
import serial
import random
import threading

guiBroker = '143.215.108.113' #Always change this to the ip address sending the info
controlBroker = '143.215.106.226' #IP address of the device the controller is connected to
port = 1883 #Port for MQTT info
videoPort = 8000 #Port for video streaming
topic1 = 'guiParseTest' #topic for Gui Data
topic2 = 'controlTest' #topic for controller data
tracker = 0
#sensorData = ''
resolution = (640,480)
framerate = 100
baudrate = 9600
timeout = 2


def initialize():
    #Initializing
    cliePub = guiPub.guiPublisher()
    clieSub = controlSub.controlSubscriber()
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
    #Connect to Arduino DUE
    clieSub.connectToDUE()
    #Connect socket for streaming
    cliePub.connectSocket(controlBroker,videoPort)
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


#All the MQTT protocols packaged into one function to be threaded
def threadedMQTTProtocols():
    while True:
        mvmntData = clieSub.receiveMvmnt()
        sensorData = clieSub.writeToDUE(mvmntData)
        g = cliePub.publishInfo(sensorData)
        print(g)

def threadedVideoProtocols(res = resolution, fr = framerate):
    cliePub.startStream(res,fr)


def main():
    #while True:
        #try:
    initialize()
        #except:
            #print("initialize failed, trying again")
    while True:
        #try:
        threading.Thread(target=threadedMQTTProtocols()).start()

        threading.Thread(target=threadedVideoProtocols()).start()
        #except:
        #initialize()

if __name__ == '__main__':
    main()
