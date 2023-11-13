import cv2
import time
import numpy as np
import sys
import datetime
import cognitive_face as CF
import sys

face_count = 0
list_anger = []
list_contempt = []
list_disgust = []
list_fear = []
list_happiness = []
list_neutral = []
list_sadness = []
list_surprise = []

def faceapi(user, s_name):
    KEY = '6ac6570cfaea47828ce0070624118f63'
    BASE_URL = 'https://japaneast.api.cognitive.microsoft.com/face/v1.0'
    global face_count
    CF.Key.set(KEY)
    CF.BaseUrl.set(BASE_URL)

    img_url = f"./{user}/{s_name}/img/user{face_count}.jpg"
    face_count = face_count + 1
    faces = CF.face.detect(img_url, attributes='emotion')
    return 0

def face_main(user, s_name): 
    global face_count
    cap = cv2.VideoCapture(0)
    ANA = 0
    time.sleep(1)
    while(cap.isOpened()):
        # フレームを取得
        ret, frame = cap.read()
        img = frame

        # フレームを表示
        cv2.imshow("Flame", frame)
        if datetime.datetime.now().second == 0 or datetime.datetime.now().second == 5 or datetime.datetime.now().second == 10 or datetime.datetime.now().second == 15 or datetime.datetime.now().second == 20 or datetime.datetime.now().second == 25 or datetime.datetime.now().second == 30 or datetime.datetime.now().second == 35 or datetime.datetime.now().second == 40 or datetime.datetime.now().second == 45 or datetime.datetime.now().second == 50 or datetime.datetime.now().second == 55:
            if ANA == 0:
                ANA = 1
                cv2.imwrite(f'./{user}/{s_name}/img/user{face_count}.jpg', img)
                face_count = face_count + 1
                time.sleep(1)
        else:
            if ANA == 1:
                ANA = 0

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    args = sys.argv
    face_main(args[1], args[2])