import serial
import time

ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=2)
message = "Left button pressed"
print(ser.in_waiting)
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
