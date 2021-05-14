import requests
from bs4 import BeautifulSoup
import win32com.client as wincL
import webbrowser
from win10toast import ToastNotifier
from notify_run import Notify
from twilio.rest import Client

notify = Notify()

toaster = ToastNotifier()

speak = wincL.Dispatch("SAPI.spVoice")

URL = 'https://www.worldometers.info/coronavirus/country/india/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
TotalCases = soup.find(class_='maincounter-number')
speak.Speak("Please enter your name")
name = input("Please enter your name: ")
speak.Speak(name + " always wear mask and properly sanitize your hand")

speak.Speak("What do you want to do")
print("1. Check statistics of Coronavirus\n2. Check statistics in webpage")
ans = int(input("1 or 2: "))

if ans == 1:
    print("Total Coronavirus cases are " + TotalCases.text)
    speak.Speak("Total Coronavirus cases are " + TotalCases.text)

    toaster.show_toast("Total Coronavirus cases",
                       TotalCases.text,
                       duration=10, icon_path="E:\PYTHON\TUTORIAL\python Basics Project\PRODUCT\Corona.ico")
    notify.send("Total coronavirus cases are: " + TotalCases.text)
    print("Sending message")

    account_sid = 'AC5e4f4d6888b075d9cc34432ac7cfa587'
    auth_token = '5a799ae3036aaa339cf3538e4bfc91df'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MGebc1a59cf707e9da000eb133ecdcb79c',
        body="Total Coronavirus cases are: "+TotalCases.text,
        to='+918348132802'
    )

    print(message.sid)
    print("Message sent")


else:
    webbrowser.open('https://www.worldometers.info/coronavirus/country/india/')
    speak.Speak("Total Coronavirus cases are " + TotalCases.text)
