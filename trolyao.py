import os
from gtts import gTTS
import playsound
import speech_recognition
from time import strftime
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import random
import re
import webbrowser
import smtplib
import urllib
import urllib.request as urllib2
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as mbox

path=ChromeDriverManager().install()
root = Tk()
text_area = Text(root, height=26, width=45)
scroll = Scrollbar(root, command=text_area.yview)

wikipedia.set_lang('ja')
language = 'ja'

def speak(text):
    print("AI:  {}".format(text))
    text_area.insert(INSERT,"AI: "+text+"\n")
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")

def get_audio():
    playsound.playsound("Ping.mp3", False)
    time.sleep(1)
    print("\nAi:  聞こえてる")
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("You: ")
        audio = r.listen(source, phrase_time_limit=6)
        try:
            text = r.recognize_google(audio, language="ja-JP")
            print(text)
            return text.lower()
        except:
            print("\n")
            return ""

def stop():
    speak("さようなら")
    time.sleep(2)

def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("聞こえない。もう一度お願いします")
            root.update()
            time.sleep(2.5)
    root.update()
    time.sleep(2)
    stop()
    return 0

def hello():
    image1 = Image.open("image\\hacker1.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("おはようございます。")
    elif 12 <= day_time < 18:
        speak("こんにちは")
    else:
        speak("こんばんは")
    root.update()
    time.sleep(5)

def get_time(text):
    image1 = Image.open("image\\thoigian.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    now = datetime.datetime.now()
    if "時" in text or "今何時" in text:
        speak('今 %d 時 %d 分' % (now.hour, now.minute))
    elif "日" in text or '日付' in text:
        speak("本日は %d年 %d 月 %d　日" %
              (now.year, now.month, now.day))
    else:
        speak("もう一度お願いします。")
        root.update()
        time.sleep(6)
    root.update()
    time.sleep(5)

def open_application(text):
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    if "google" in text:
        speak(" グーグルクローム")
        time.sleep(2)
        os.startfile('"C:\Program Files\Google\Chrome\Application\chrome.exe"')
    elif "word" in text:
        speak("ワード")
        time.sleep(2)
        os.startfile('C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE')
    elif "excel" in text:
        speak("エクセル")
        time.sleep(2)
        os.startfile('C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE')
    elif "code" in text:
        speak("コード")
        time.sleep(2)
        os.startfile('C:\VSCode-win32-x64-1.55.0\Code.exe')
    else:
        speak("アプリケーションがインストールされていません。もう一度やり直してください！")
    root.update()
    time.sleep(6)

def open_website(text):
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    reg_ex = re.search('ウェブサイト (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain + '.com'
        webbrowser.open(url)
        speak("開きました")
        root.update()
        time.sleep(5)
        return True
    else:
        return False
   

def weather(text):
    temp="Trời quang mây tạnh"
    if "moderate rain" in text:
        temp="Trời hôm nay có mưa vừa, bạn ra ngoài nhớ mang theo áo mưa" 
    elif "heavy intensity rain" in text or "thunderstorm with light rain" in text or "very heavy rain" in text:
        temp="Trời hôm nay có mưa rất lớn kèm theo giông sét, bạn nhớ đem ô dù khi ra ngoài" 
    elif "light rain" in text:
        temp="Trời hôm nay mưa nhẹ, rải rác một số nơi" 
    elif "heavy intensity shower rain" in text:
        temp="Trời hôm nay có mưa rào với cường độ lớn"
    elif "broken clouds" in text or "few clouds" in text:
        temp="Trời hôm nay có mây rải rác, không mưa"
    elif "overcast clouds" in text:
        temp="Trời hôm nay nhiều mây, u ám, dễ có mưa"
    elif "scattered clouds" in text:
        temp="Trời hôm nay có nắng, có mây rải rác"   
    
    if "rain" in text:
        image1 = Image.open("image\\thoitiet2.jpg")
        image_1 = ImageTk.PhotoImage(image1)    
        label1 = Label(image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)
    else :
        image1 = Image.open("image\\thoitiet1.jpg")
        image_1 = ImageTk.PhotoImage(image1)    
        label1 = Label(image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)

    return temp

def temperature(text):
    temp="mát mẻ"
    if text<15:
        temp="lạnh buốt giá"
    elif text<20:
        temp="khá lạnh"
    elif text<30:
        temp="mát mẻ"
    elif text<33:
        temp="khá nóng"
    else:
        temp="nóng bức"

    return temp

def current_weather():
    speak("どこで天気を見たいですか？")
    root.update()
    time.sleep(3)
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_audio()
    text_area.insert(INSERT,"You: "+city+"\n")
    if city=="":
        current_weather()
    else:
        api_key = "b0d4f9bfd2bbc40d10976e6fd3ea7514"
        call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
        response = requests.get(call_url)
        data = response.json()
        if data["cod"] != "404":
            city_res = data["main"]
            current_humidity = city_res["humidity"]
            current_temperature = city_res["temp"]
            current_pressure = city_res["pressure"]
            temperature1=temperature(current_temperature)
            suntime = data["sys"]
            sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
            sunset = datetime.datetime.fromtimestamp(suntime["sunset"])

            weather_description = data["weather"][0]["description"]
            weather1=weather(weather_description)
            now = datetime.datetime.now()
            wthr = data["weather"]
            content = """
            本日は {year}年{month}月{day}日　
            日の出は{hourrise}時{minrise}分に昇ります
            日没は{hourset}時{minset}分に沈みます
            平均気温は{temp}℃です
            気圧は{pressure}パスカルです
            湿度は{humidity}％です
            今日はいい天気ですから、散歩しましょう.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)

            speak(content)
            root.update()
            time.sleep(2)
        else:
            speak("住所が見つかりませんでした")
            root.update()
            time.sleep(2)
            current_weather()

def sleep_time(x):
    if x==1:
        time.sleep(13)
    elif x==2:
        time.sleep(10)
    elif x==3:
        time.sleep(7)
    elif x==4:
        time.sleep(13)
    elif x==5:
        time.sleep(11)
    elif x==6:
        time.sleep(11)
    else :
        time.sleep(21)


def get_math():
    speak("計算します")
    root.update()
    time.sleep(4)
    text1=get_audio()
    text_area.insert(INSERT,"You: "+text1+"\n")
    root.update()
    image_1 = ImageTk.PhotoImage(Image.open("image\\math.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    if "+" in text1 or "加算" in text1:
        text2=text1.replace("+", "-")
        try:
            math_a = re.search('(.+) -', text2)
            a = math_a.group(1)
            math_b = re.search('- (.+)', text2)
            b = math_b.group(1)
            c = float(a)+float(b)
            speak("結果 "+a+" プラス "+b+" イコール: "+str(c))
            root.update()
        except:
            speak("計算が無効です")
            root.update()
    elif "/" in text1 or "割り算" in text1:
        text2=text1.replace("割り", "/")
        try:
            math_a = re.search('(.+) /', text2)
            a = math_a.group(1)
            math_b = re.search('/ (.+)', text2)
            b = math_b.group(1)
            c = float(a)/float(b)
            speak("結果 "+a+" わる "+b+" イコール: "+str(c))
            root.update()
            time.sleep(3)
        except:
            speak("計算が無効です")
            root.update()

    elif "x" in text1 or "乗算" in text1:
        text2=text1.replace("乗算", "x")
        try:
            math_a = re.search('(.+) x', text2)
            a = math_a.group(1)
            math_b = re.search('x (.+)', text2)
            b = math_b.group(1)
            c = float(a)*float(b)
            speak("結果 "+a+" 掛ける "+b+" イコール: "+str(c))
            time.sleep(2)
            root.update()
        except:
            speak("計算が無効です")
            root.update()
    elif "-" in text1 or "引き算" in text1:
        try:
            math_a = re.search('(.+) - ', text1)
            a = math_a.group(1)
            math_b = re.search(' - (.+)', text1)
            b = math_b.group(1)
            c = float(a)-float(b)
            speak("結果 "+a+" 引く "+b+" イコール: "+str(c))
            root.update()
        except:
            speak("計算が無効です")
            root.update()
    else:
        speak("計算が無効です")
        root.update()
    
    time.sleep(6)


def youtube_search():
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    speak('内容をお選びください')
    root.update()
    time.sleep(2)
    text = get_audio()
    text_area.insert(INSERT,"You: "+text+"\n")
    root.update()
    if text == "":
        speak("検索エラー")
        root.update()
        time.sleep(4)
    else:
        search = SearchVideos(text, offset = 1, mode = "json", max_results = 20).result()
        data = json.loads(search)
        url = data["search_result"][0]["link"]
        print(url)
        webbrowser.open(url)
        speak("リクエストしたビデオが再生されました。")
        root.update()
        time.sleep(7)   

def tell_me_about():
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    try:
        speak("何について聞きたいですか？")
        root.update()
        time.sleep(2)
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0].split(".")[0])
        root.update()
        time.sleep(20)
        for content in contents[1:]:
            speak("もっと聞きたいですか？")
            root.update()
            time.sleep(2)
            ans = get_text()
            if "はい" not in ans:
                break    
            speak(content)
            root.update()
            time.sleep(10)
    except:
        speak("ボットはあなたの用語を定義しません。 もう一度言ってください")
        root.update()
        time.sleep(5)

def func():
    image1 = Image.open("image\\trolyao.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    content="""
    私は次の機能を持っています:
    1.挨拶
    2.通知時間 
    3.天気予報 
    4.簡単な計算
    5.アプリを開き、ウェブサイトを開きます
    6.グーグルで情報を検索 
    7.YouTubeで音楽、ビデオを開く
    8.Wikipediaで情報を探す
    """
    speak(content)
    root.update()
    time.sleep(30)

def color():
    mylist = ["#009999","black","green","grey","blue","orange","#cc0099","#00ff00","brown"]
    aa=random.choice(mylist)
    text_area.tag_add("here", "1.0", "100000.0")
    text_area.tag_config("here", background = aa)
    root.update()

def color1():
    mylist1 = ["yellow","#0000ff","white","#00ff00","black"]
    bb=random.choice(mylist1)
    text_area.tag_add("here", "1.0", "100000.0")
    text_area.tag_config("here",foreground = bb)
    root.update()

def info():
    mbox.showinfo("案内", "-マイクを押して、AIと話し始める.\n-更新を押して会話全体をクリアします.\n-背景色やテキストの色をランダムに変更できます.\n-AIがあなたの話を聞いていると、ピップ音が鳴ります.\n-会話を保留にするには、「ストップ」と言います.\n-終了を押してプログラムを閉じます.")

def r_set():
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    text_area.delete("1.0", "1000000000.0")

def ham_main():
    speak("こんにちは。何か助けますか?")
    root.update()
    time.sleep(2)
    r = speech_recognition.Recognizer()
    you=""
    ai_brain=""
    while True:
        with speech_recognition.Microphone() as source:
            playsound.playsound("Ping.mp3", False)
            time.sleep(1)
            print("AI:  聞こえてる ...")
            audio = r.listen(source, phrase_time_limit=6)
            print("AI:  ...")
        try:
            you = r.recognize_google(audio, language="ja-JP")
            print("\nYou: "+ you)	
            you = you.lower()
        except:
            ai_brain = "聞こえない。もう一度お願いします"
            print("\nAI: " + ai_brain)

        text_area.insert(INSERT,"You: "+you+"\n")
        root.update()

        if "おはようございます" in you or "hello" in you or "こんにちは" in you or "こんばんは" in you or "hi" in you:
            hello()
        elif "天気" in you:
            current_weather()
            break
        elif "何日" in you or "何時" in you or "日付" in you:
            get_time(you)
        elif "計算"in you :
            get_math()
        elif "アプリ" in you:
            speak("開きたいアプリの名前は")
            time.sleep(3)
            text1 = get_text()
            open_application(text1)
            break
        elif "ウェブサイト" in you:
            open_website(you)
            break
        elif "音楽" in you or "youtube" in you or "ビデオ" in you:
            youtube_search()
            break
        elif "機能" in you or "できます" in you:
            func()
        elif "背景色変更" in you:
            color()
        elif "テキスト色変更" in you:
            color1()
        elif "ウィキペディア" in you or "wikipedia" in you:
            tell_me_about()
            break
        elif "ストップ"  in you or "うるさい" in you:
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            break
        elif "またね" in you or "さようなら" in you or "ありがとう" in you or "どうも" in you:
            ai_brain="喜んでお手伝いいたします。ありがとうございました。"
            speak(ai_brain)
            root.update()
            time.sleep(4)
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            playsound.playsound("Ping.mp3", False)
            time.sleep(1)
            exit()
        else:
            ai_brain = "聞こえない。もう一度お願いします"
            speak(ai_brain)
            root.update()
            time.sleep(2.5)

        text_area.insert(INSERT,"_____________________________________________")
        you=""

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent) 
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("AI サポータ by AHIHI TEAM")
        self.style = Style()
        self.style.theme_use("default")
        
        scroll.pack(side=RIGHT, fill=Y)
        text_area.configure(yscrollcommand=scroll.set)
        text_area.pack(side=RIGHT)

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)


        closeButton = Button(self, text="終了",command = exit,width=10,fg="white", bg="#009999",bd=3)
        closeButton.pack(side=RIGHT, padx=11, pady=10)
        okButton = Button(self, text="マイク",command = ham_main,width=10,fg="white", bg="#009999",bd=3)
        okButton.pack(side=RIGHT, padx=11, pady=10)
        doimau = Button(self,text="背景色変更",command = color,width=10,fg="white", bg="#009999",bd=3)
        doimau.pack(side=RIGHT,padx=11, pady=10)
        doimau = Button(self,text="テキスト色変更",command = color1,width=10,fg="white", bg="#009999",bd=3)
        doimau.pack(side=RIGHT,padx=11, pady=10)
        thongtin = Button(self,text="案内",command = info,width=10,fg="white", bg="#009999",bd=3)
        thongtin.pack(side=RIGHT,padx=11, pady=10)
        lammoi = Button(self,text="更新",command = r_set,width=10,fg="white", bg="#009999",bd=3)
        lammoi.pack(side=RIGHT,padx=11, pady=10)

        # self.pack(fill=BOTH, expand=1)   
        # Style().configure("TFrame", background="#333")
    
        image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
        label1 = Label(self, image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)

        l = Label(root, text='チャット履歴', fg='White', bg='blue')
        l.place(x = 750, y = 10, width=120, height=25)
        l1 = Label(root, text='AI サポータ by AHIHI TEAM ', fg='yellow', bg='black')
        l1.place(x = 250, y = 11, width=150, height=25)

root.geometry("1000x510+250+50")
root.resizable(False, False)
app = Example(root)
root.mainloop()

#http://api.openweathermap.org/data/2.5/weather?appid=b0d4f9bfd2bbc40d10976e6fd3ea7514&q=da%20nang&units=metric