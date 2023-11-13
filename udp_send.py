import socket
import time
from threading import (Event, Thread)
import output_audio
import serial_arduino
import user_audio
from playsound import playsound

id = 0
talks = ""
texts = []
checks = 0

def udp_send(param, user, s_name):
    HOST = '127.0.0.1'
    PORT=50007
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    result = str(param)
    if result == "301" or result == "302" or result == "303":
        client.sendto(result.encode('utf-8'),(HOST,PORT))
        client.close()
    else:
        time.sleep(30)
        playsound("botan.mp3")
        client.sendto(result.encode('utf-8'),(HOST,PORT))
        client.close()

    udp_receive(user, s_name)
    

def udp_receive(user, s_name):
    address = ('127.0.0.1', 50008)
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #udpという名前のUDPソケット生成
    udp.bind(address) #udpというソケットにaddressを紐づける
    #udp.setblocking(0)
    output_count = 0

    while True: #受信ループ
        try:
            global id, talks, texts, checks
            rcv_byte = bytes() #バイトデータ受信用変数
            rcv_byte, addr = udp.recvfrom(1024) #括弧内は最大バイト数設定
            msg = rcv_byte.decode(encoding='utf-8') #バイトデータを文字列に変換
            print(msg) #文字列表示
            if checks == 0:
                id = msg
                checks = 1
            elif checks == 1:
                texts.append(msg)
                if id == "0":
                    serial_arduino.out_180()
                    checks = 0
                elif id == "1":
                    serial_arduino.out_0()
                    checks = 0
                elif id == "10":
                    user_audio.user_audio(user, s_name)
                    checks = 0
                else:
                    output_audio.text_to_speech(output_count, texts, id, user, s_name)
                    output_count = output_count + 1
                    checks = 0
                texts = []
        except KeyboardInterrupt:#強制終了を検知したらUDPソケットを閉じて終了
            udp.close()
