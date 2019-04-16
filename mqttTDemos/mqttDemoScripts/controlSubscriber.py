import clientObjClass as cli
import pdb
import serial
import time


class controlSubscriber(object):

    def __init__(self):
        self.__connectionStatus = False
        clientObj = cli.clientObjClass()
        self.__clientObj = clientObj
        self.__serial_port = ''

    def getClient(self):
        a = self.__clientObj.getClient()
        return(a)

    def buildSubscriber(self):
        self.__clientObj.createClient()

    def addSubscriberParams(self,broker,port,topic):
        self.__clientObj.setClientParams(broker,port,topic)

    def connectSubscriber(self):
        self.__clientObj.connectClient()
        self.__connectionStatus = True

    def setSerialPort(self,serialPort):
        self.__serial_port = serialPort

    def receiveMvmnt(self):
        subscribedData = self.__clientObj.printFromSubscriber()
        print('subscribed Data')
        self.__sensorDataPreParse = subscribedData.payload
        return(self.__sensorDataPreParse)

    def foreverLoopClient(self):
        self.__clientObj.loopClientForever()

    def startSubscribeLoop(self,indicator):
        self.__clientObj.startLoop(indicator)

    def stopSubscribeLoop(self):
        self.__clientObj.endLoop()

    def checkConnection(self):
        return(self.__connectionStatus)

    def checkClientDetails(self):
        details = self.__clientObj.getClientParams()
        return(details)

    def writeToDUE(self,mvmntMsg):
        #Adding the serial write method here to write to the motors
        #on the Arduino DUE

        print('wrote to DUE')
<<<<<<< HEAD
        ser = serial.Serial(port='COM8', baudrate=9600, timeout=2)

        while True:
            while (ser.in_waiting>0):
                print("in: "+str(ser.in_waiting))
                ser.reset_input_buffer()
                time.sleep(.01)
            while (ser.out_waiting>0):
                print("out: "+str(ser.out_waiting))
                ser.reset_output_buffer()
                time.sleep(.01)
            ser.write(message.encode())
            print("message sent")
            data = ser.readline()
            if data or True:
                print(data.decode())
            else:
                print('nothing')
=======
        ser = serial.Serial(port= self.__serial_port, baudrate=9600, timeout=2)

        while (ser.in_waiting>0):
            print("in: "+str(ser.in_waiting))
            ser.reset_input_buffer()
            time.sleep(.01)
        while (ser.out_waiting>0):
            print("out: "+str(ser.out_waiting))
            ser.reset_output_buffer()
            time.sleep(.01)
        ser.write(mvmntMsg.encode())
        print("message sent")
        data = ser.readline()
        if data or True:
            print(data.decode())
        else:
            print('nothing')
>>>>>>> 05766dded5791aef0282cad83109a827d4d1c753
