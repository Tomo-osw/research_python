import requests
import json
import time
import wave
import numpy as np
import glob
from playsound import playsound
import os

def combine(output_count, user, s_name):
    audios = []
    for f in sorted(glob.glob(f"./{user}/{s_name}/output_wav/audio_{output_count}_*.wav")):
        with wave.open(f, "rb") as fp:
            buf = fp.readframes(-1) # 全フレーム読み込み
            assert fp.getsampwidth() == 2 # と仮定（np.int16でキャスト）
            audios.append(np.frombuffer(buf, np.int16))
            params = fp.getparams()
    audio_data = np.concatenate(audios)
    # 正規化（ピーク時基準）
    scaling_factors = [np.iinfo(np.int16).max/(np.max(audio_data)+1e-8),
                       np.iinfo(np.int16).min/(np.min(audio_data)+1e-8)]
    # s>0:位相が反転しないようにする。ここをmaxにするとプチッというノイズが入るので注意
    scaling_factors = min([s for s in scaling_factors if s > 0]) 
    audio_data = (audio_data * scaling_factors).astype(np.int16)
    with wave.Wave_write(f"./{user}/{s_name}/output_wav/return{output_count}.wav") as fp:
        fp.setparams(params)
        fp.writeframes(audio_data.tobytes())
    
    os.chdir(f'./{user}/{s_name}/output_wav/')
    playsound(f"return{output_count}.wav")
    os.chdir('../../../')


# VoicevoxでText to Speechするやつ
def synthesis(text, filename, speaker, max_retry=20):
    # Internal Server Error(500)が出ることがあるのでリトライする
    # （HTTPAdapterのretryはうまくいかなかったので独自実装）
    # connect timeoutは10秒、read timeoutは300秒に設定（処理が重いので長めにとっておく）
    # audio_query
    query_payload = {"text": text, "speaker": speaker}
    for query_i in range(max_retry):
        r = requests.post("http://localhost:50021/audio_query", 
                        params=query_payload, timeout=(10.0, 300.0))
        if r.status_code == 200:
            query_data = r.json()
            break
        time.sleep(1)
    else:
        raise ConnectionError("リトライ回数が上限に到達しました。 audio_query : ", filename, "/", text[:30], r.text)

    # synthesis
    synth_payload = {"speaker": speaker}    
    for synth_i in range(max_retry):
        r = requests.post("http://localhost:50021/synthesis", params=synth_payload, 
                          data=json.dumps(query_data), timeout=(10.0, 300.0))
        if r.status_code == 200:
            with open(filename, "wb") as fp:
                fp.write(r.content)
            print(f"{filename} は query={query_i+1}回, synthesis={synth_i+1}回のリトライで正常に保存されました")
            break
        time.sleep(1)
    else:
        raise ConnectionError("リトライ回数が上限に到達しました。 synthesis : ", filename, "/", text[:30], r,text)

def text_to_speech(output_count, texts, speaker, user, s_name):
    #※テキストはイメージです
    #texts = [
    #    "おはようございます。こんにちは！大丈夫ですかあ？？？"
    #]
    for i, t in enumerate(texts):
        synthesis(t, f"./{user}/{s_name}/output_wav/audio_{output_count}_{i}.wav",speaker)
    
    combine(output_count, user, s_name)

if __name__ == "__main__":
    texts = []
    texts.append("おはようございます。えーと、、、大丈夫ですか！！！！？")
    #text_to_speech(1, texts, 23)
    text_to_speech(2, texts, 24)
    #text_to_speech(3, texts, 25)
    #text_to_speech(4, texts, 26)