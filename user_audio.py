from multiprocessing.spawn import import_main_path
import cv2
import time
import numpy as np
import sys
import datetime
import pyaudio  #録音機能を使うためのライブラリ
import wave     #wavファイルを扱うためのライブラリ
import requests
import sys
import os

audio_count = 0

def user_audio(user, s_name):
    global audio_count
    RECORD_SECONDS = 7 #録音する時間の長さ（秒）
    iDeviceIndex = 0 #録音デバイスのインデックス番号

    #基本情報の設定
    FORMAT = pyaudio.paInt16 #音声のフォーマット
    CHANNELS = 1             #モノラル
    RATE = 11025             #サンプルレート
    CHUNK = 2**11            #データ点数
    audio = pyaudio.PyAudio() #pyaudio.PyAudio()
    
    stream = audio.open(format=FORMAT, channels=CHANNELS,
            rate=RATE, input=True,
            input_device_index = iDeviceIndex, #録音デバイスのインデックス番号
            frames_per_buffer=CHUNK)

    #--------------録音開始---------------
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    #--------------録音終了---------------
    
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    waveFile = wave.open(f"./{user}/{s_name}/input_user_audio/user{audio_count}.wav", 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    audio_count = audio_count + 1

if __name__ == "__main__":
    args = sys.argv
    user_audio(args[1], args[2])