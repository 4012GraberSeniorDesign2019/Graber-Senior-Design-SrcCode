import clientObjClass as cli
import pdb
import time
import random
import socket
import struct
import picamera
import io
import serial

class guiPublisher(object):

    def __init__(self):
        self.__connectionStatus = False
        clientObj = cli.clientObjClass()
        self.__clientObj = clientObj
        self.__client_socket = ''
        self.__serialPort = ''

    def getClient(self):
        a = self.__clientObj.getClient()
        return(a)

    def buildPublisher(self):
        self.__clientObj.createClient()

    def addPublisherParams(self,broker,port,topic):
        self.__clientObj.setClientParams(broker,port,topic)

    def buildSocket(self):
        self.__client_socket = socket.socket()

    def connectSocket(self,broker,port):
        self.__client_socket.connect((broker,port))

    def connectPublisher(self):
        self.__clientObj.connectClient()
        self.__connectionStatus = True

    def startPublishLoop(self,indicator):
        self.__clientObj.subscribeToTopic()
        status = self.__clientObj.startLoop(indicator)

    def stopPublishLoop(self):
        status = self.__clientObj.endLoop()

    def publishInfo(self,data):
        print('Assigned Sensor Data')
        a = self.__clientObj.publishData(data)
        return(a)

    def connectSerialPort(self,baudRate,timeOut):
        ser = serial.Serial(self.__serialPort,baudrate = baudRate,timeout = timeOut)
        self.__ser = ser
        ser.open()
        return(ser.is_open())

    def readSerialPort(self):
        a = self.__ser.read()
        return(a)

    def startStream(self,res,frameRate):
        try:
            with picamera.PiCamera(resolution = res,framerate = frameRate) as camera:
                # Start a preview and let the camera warm up for 2 seconds
                #camera.start_preview()
                #time.sleep(2)

                #Note the start time and construct a stream to hold image Data
                #temporarily (we could write it directly to connection but in this
                # case we want to find out the size of each capture first to keep
                # our protocol simple)
                start = time.time()
                stream = io.BytesIO()
                for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                    # Write the length of the capture to the stream and flush to
                    # ensure it actually gets sent
                    connection.write(struct.pack('<L', stream.tell()))
                    connection.flush()
                    #Rewind the stream and send the image data over the wire
                    stream.seek(0)
                    connection.write(stream.read())

                    #Reset the stream for the next capture_continuous
                    stream.seek(0)
                    stream.truncate()

                #Write a length of zero to the stream to signal we're done
            connection.write(struct.pack('<L',0))
        finally:
            connection.close()
            self.__client_socket.close()

    def checkConnection(self):
        return(self.__connectionStatus)

    def checkClientDetails(self):
        details = self.__clientObj.getClientParams()
        return(details)

    def foreverLoopClient(self):
        self.__clientObj.loopClientForever()
