import serial
import time

def out_180():
    ser_1 = serial.Serial("COM4", 9600, timeout = 0.1)
    ser_2 = serial.Serial("COM3", 9600, timeout = 0.1)
    ser_3 = serial.Serial("COM5", 9600, timeout = 0.1)
    time.sleep(2) 
    ser_1.write(bytes("s",'utf-8'))
    ser_2.write(bytes("s",'utf-8'))
    ser_3.write(bytes("s",'utf-8'))
    ser_1.close()
    ser_2.close()
    ser_3.close()

def out_0():
    ser_1 = serial.Serial("COM4", 9600, timeout = 0.1)
    ser_2 = serial.Serial("COM3", 9600, timeout = 0.1)
    ser_3 = serial.Serial("COM5", 9600, timeout = 0.1)
    time.sleep(2) 
    ser_1.write(bytes("a",'utf-8'))
    ser_2.write(bytes("a",'utf-8'))
    ser_3.write(bytes("a",'utf-8'))
    ser_1.close()
    ser_2.close()
    ser_3.close()

if __name__ == "__main__":
    out_0()
    time.sleep(3) 
    out_180()
    time.sleep(3) 
    out_0()
    time.sleep(3) 
    out_180()
    time.sleep(3) 
    out_0()
    time.sleep(3) 
    out_180()
    time.sleep(3) 
    out_0()