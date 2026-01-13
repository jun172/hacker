import random
import time

# ランプの色
colors = ["赤", "緑", "黄"]

# ゲーム回数
rounds = 5
score = 0

print("フラッシュ計算風ゲーム開始！")
print("光った色を素早く入力してください。")

for i in range(rounds):
    time.sleep(random.uniform(1, 3))  # ランダムに待機
    lamp = random.choice(colors)
    print(f"\nランプ: {lamp}")

    user_input = input("色を入力: ")

    if user_input == lamp:
        print("✅ 正解！")
        score += 1
    else:
        print("❌ 間違い！")

print(f"\nゲーム終了!スコア: {score}/{rounds}")

from flask import Flask
app=False(__name__)

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Book

def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    return HttpResponse(f"{book.title} - {book.author} - {book.price}円")

from django import forms
from .models import book
class Bools(forms.ModelForm):
    class Meta:
        model=Book
        fiend=["title","author","price"]
        
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title

from django.shortcuts import render
from .models import Book

def book_list(request):
    # DB から全件取得してテンプレートに渡す
    books = Book.objects.all().order_by('id')
    return render(request, "home/book_list.html", {"books": books})

# aht20_ex1_esp32.py
import machine
import time
import neopixel
from ahtx0 import AHTx0  # MicroPython用AHT20ドライバ

# I2C設定
i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
sensor = AHTx0(i2c)

# NeoPixel設定（LED1個をGPIO4に接続）
np = neopixel.NeoPixel(machine.Pin(4), 1)

# 不快指数データ
discomfort_index_data = [
    (55, "寒い", (0, 0, 128)),
    (60, "肌寒い", (0, 64, 128)),
    (65, "何も感じない", (0, 128, 128)),
    (70, "快い", (0, 128, 0)),
    (75, "暑くない", (128, 128, 0)),
    (80, "やや暑い", (128, 64, 0)),
    (85, "暑くて汗が出る", (128, 32, 0)),
    (float('inf'), "暑くてたまらない", (128, 0, 0)),
]

while True:
    temperature, humidity = sensor.temperature, sensor.relative_humidity

    # 不快指数の計算
    discomfort_index = 0.81 * temperature + 0.01 * humidity * (0.99 * temperature - 14.3) + 46.3

    # 該当体感とRGBを取得
    for threshold, feeling, rgb in discomfort_index_data:
        if discomfort_index <= threshold:
            print(f"不快指数: {discomfort_index:.2f} → 体感: {feeling}")
            np[0] = rgb
            np.write()  # LEDに色を反映
            break

    time.sleep(2)  # 2秒ごとに更新

