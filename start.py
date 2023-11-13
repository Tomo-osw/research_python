from hmac import trans_36
from multiprocessing.spawn import import_main_path
import input_face
import input_audio
import input_openbci
import udp_send
import time
import sys
import os

def main(user, s_name, s_number):
    #最初にファイル生成を設定する
    if os.path.isdir(f"./{user}"):
        os.chdir(f"./{user}")
    else:
        os.mkdir(f"./{user}")
        os.chdir(f"./{user}")
    
    if os.path.isdir(f"./{s_name}"):
        os.chdir("../")
    else:
        os.mkdir(f"./{s_name}")
        os.chdir(f"./{s_name}")
        os.mkdir("./wav")
        os.mkdir("./output_wav")
        os.mkdir("./img")
        os.mkdir("./openbci")
        os.mkdir("./input_user_audio")
        os.chdir("../")
        os.chdir("../")

    time.sleep(5)
    udp_send.udp_send(s_number, user, s_name)
    
    #スレッド設定
    #with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        #音声解析
        #要API再設定→月300回まで
        #executor.submit(input_audio.rokuon(user, s_name))
        
        #顔表情解析
        #executor.submit(input_face.face_main(user, s_name))

        #脳波取得
        #executor.submit(input_openbci.main(user, s_name))
        
        #unityとの通信_引数が実験番号
        #executor.submit(udp_send.udp_send(s_number, user, s_name))


if __name__ == "__main__":
    args = sys.argv
    if 4 == len(args):
        time.sleep(8)
        main(args[1], args[2], args[3])
    else:
        print('引数は3つ、ユーザ(P0)と実験用(S0)と実験番号(000)を指定してください')