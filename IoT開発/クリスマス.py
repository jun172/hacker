from machine import Pin, time_pulse_us, PWM
from neopixel import NeoPixel
from time import sleep, sleep_us
import random

# --- GPIO設定 ---
LED_PIN = 10 #  NeoPixel のデータピン
NUM_LEDS = 63 # LED数
TRIG_PIN = 4#超音波センサー TRIG
ECHO_PIN = 5 # 超音波センサー ECHO
SPEAKER_PIN = 21 # ブザー / スピーカー

# --- 初期化 ---
leds = NeoPixel(Pin(LED_PIN, Pin.OUT), NUM_LEDS)# NeoPixel 初期化
trig = Pin(TRIG_PIN, Pin.OUT)# 超音波センサー初期化
echo = Pin(ECHO_PIN, Pin.IN)# PWMスピーカー初期化
speaker = PWM(Pin(SPEAKER_PIN))
DUTY = 47828 #73% PWM  音量調整
speaker.duty_u16(0)  # 最初は無音

# --- 音階 ---
notes = {
    "C4": 262, "D4": 294, "E4": 330,
    "F4": 349, "G4": 392, "A4": 440,
    "B4": 494, "C5": 523,
    "D5": 587, "E5": 659, "F5": 698,
    "G5": 784, "A5": 880
}


# --- ジングルベルメロディ ---
melody = [
    ("E4",0.25),("E4",0.25),("E4",0.5),
    ("E4",0.25),("E4",0.25),("E4",0.5),
    ("E4",0.25),("G4",0.25),("C4",0.25),("D4",0.25),("E4",1.0),
    ("F4",0.25),("F4",0.25),("F4",0.5),
    ("F4",0.25),("E4",0.25),("E4",0.5),
    ("E4",0.25),("E4",0.25),("E4",0.5),
    ("E4",0.25),("D4",0.25),("D4",0.5),
    ("E4",0.5),("G4",0.25),("G5",1.0),
]*1
 
# --- BPM設定 --- 
BPM = 82
beat_duration = 60 / BPM  # 1拍の秒数

# --- 距離取得 ---
def measure():
    trig.off() # TRIG初期化
    sleep_us(2)
    trig.on()
    sleep_us(10)# 10usパルス送信
    trig.off()

    # timeout を 30ms → 60ms に増加
    duration = time_pulse_us(echo, 1, 60000)

    if duration < 0:
        return None

    # 距離[m]
    distance_m = (duration / 2) / 29.1 / 100#音速から距離算出

    return max(distance_m, 0)  # 0未満防止 

# --- LED全灯クリスマス色ランダム ---
def christmas_all_leds():
    colors = [(255,0,0), (0,255,0), (255,215,0), (255,255,255)]  # 赤・緑・金・白
    for i in range(NUM_LEDS):# 全LEDランダム点灯
        leds[i] = random.choice(colors)
    leds.write() # LED更新
    sleep(0.05) # 少し待機

# --- 音を鳴らす ---
def play_note(note, duration):
    freq = notes.get(note, 0)  # 音階から周波数取得
    if freq > 0: # 音が存在する場合
        speaker.freq(freq) # 周波数設定
        speaker.duty_u16(DUTY) # 音量ON
        sleep(duration)# 音長
        speaker.duty_u16(0) # 音停止
    else:
        sleep(duration)
        
# --- メロディ再生（LED全灯＋ピカピカ＋距離表示） ---
def play_melody():
    while True:
        distance = measure()# 距離測定
        if distance is not None:    # 距離表示
            print("Distance: {:.2f} m".format(distance))  # 距離表示
        else:
            print("Out of range")
        
        if distance is not None and distance <=1.5:#1.5m以内なら再生
            for note, duration in melody:# メロディループ
                play_note(note, duration)# 音再生
                christmas_all_leds()   # LED演出
        else:
            leds.fill((0,0,0))# LED消灯
            leds.write()
            sleep(0.1)
            
# --- 実行 ---
try:
    play_melody()
except KeyboardInterrupt:# Ctrl + C 停止時
    leds.fill((0,0,0)) # LED消灯
    leds.write()
    speaker.duty_u16(0)# 音停止
    
    print("Stopped")