import socket
import random
import time

def face_udp(ang, con, dis, fea, hap, neu, sad, sur):
    HOST = '127.0.0.1'
    PORT=50007
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    times = 0
    while times < 9:
        if times == 1:
            result = str(ang)
            client.sendto(result.encode('utf-8'),(HOST,PORT))
        
        if times == 2:
            result = str(con)
            client.sendto(result.encode('utf-8'),(HOST,PORT))

        if times == 3:
            result = str(dis)
            client.sendto(result.encode('utf-8'),(HOST,PORT))

        if times == 4:
            result = str(fea)
            client.sendto(result.encode('utf-8'),(HOST,PORT))

        if times == 5:
            result = str(hap)
            client.sendto(result.encode('utf-8'),(HOST,PORT))

        if times == 6:
            result = str(neu)
            client.sendto(result.encode('utf-8'),(HOST,PORT))

        if times == 7:
            result = str(sad)
            client.sendto(result.encode('utf-8'),(HOST,PORT))

        if times == 8:
            result = str(sur)
            client.sendto(result.encode('utf-8'),(HOST,PORT))

        if times == 9:
            result = str("0")
            client.sendto(result.encode('utf-8'),(HOST,PORT))
            
        times = times + 1
    
    times = 0

def rokuon_udp(cal, ang2, joy, sor, ene):
    HOST = '127.0.0.1'
    PORT=50007
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    times2 = 0
    while times2 < 6:
        if times2 == 1:
            result = str(cal)
            client.sendto(result.encode('utf-8'),(HOST,PORT))

        if times2 == 2:
            result = str(ang2)
            client.sendto(result.encode('utf-8'),(HOST,PORT))

        if times2 == 3:
            result = str(joy)
            client.sendto(result.encode('utf-8'),(HOST,PORT))

        if times2 == 4:
            result = str(sor)
            client.sendto(result.encode('utf-8'),(HOST,PORT))

        if times2 == 5:
            result = str(ene)
            client.sendto(result.encode('utf-8'),(HOST,PORT))

        if times2 == 6:
            result = str("0")
            client.sendto(result.encode('utf-8'),(HOST,PORT))
            
        times2 = times2 + 1
    
    times2 = 0