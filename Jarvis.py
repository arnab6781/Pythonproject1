import win32com.client as wincL
import datetime
import os
import webbrowser

f = open("detail.txt")
content = f.read()

speak = wincL.Dispatch("SAPI.spVoice")
time = int(datetime.datetime.now().hour)
if 0 <= time < 12:
    speak.Speak("Good Morning")
elif 12<= time <18:
    speak.Speak("Good afternoon")
else:
    speak.Speak("Good night")   
speak.Speak("My name is Jarvis and I am a virtual assistant created by Arnab Maity")
speak.Speak("Can you tell me your name?")
name = input("Please enter your name: ")
speak.Speak("Welcome "+ name)
speak.Speak("What I can do for you?")
print("==================\n1.Show Arnab Details\n2.Open Camera folder\n3.Open Music folder\n4.Tell a joke\n5.Open Documents folder\n6.Check Whether\n7.Check mail\n8.Check Covid-19 status\n9.Open youtube\n10.Famous Persons\n11.play funny video\n==================")
ans = int(input("Enter a number from the list: "))
if ans == 1:
    speak.Speak("You have to enter password to see Arnab's details")
    password =  input("Please enter password: ")
    if password == "arnabmaity":
      speak.Speak("Ok " + name + " here is Arnab's details")
      print(content)
    else:
        print("Wrong password------------\n  Program Terminated")  
        speak.Speak("Sorry I think you are a Imposter. You cannot do this but you can try other activities")
elif ans == 2:
    speak.Speak("Ok " + name + " now I am going to open the Camera folder")
    os.startfile("D:\Camera") 
elif ans == 3:
    speak.Speak("Ok " + name + " here is the music folder")
    os.startfile("D:\music")
elif ans == 4:
    speak.Speak(name + " You are the most beautiful man of earth")
elif ans  == 5:
    speak.Speak("Ok " + " Here is the document folder")
    os.startfile("D:\Documents")
elif ans == 6:
    speak.Speak("Opening wheather.com")
    print("Opening weather.com")
    webbrowser.open("https://weather.com/en-IN/weather/today/l/22.53,87.90?par=google&temp=c") 
elif ans == 7:
    speak.Speak("Checking mail")
    print("opening Mail------")
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
elif ans == 8:
    speak.Speak(name + " always wear mask and properly sanitize your hands")
    speak.Speak("Checking Corona Virus Status")
    print("Checking Covid-19 Status---------")
    webbrowser.open("https://www.covid19india.org/")        
elif ans == 9:
    webbrowser.open("https://www.youtube.com")
elif ans == 10:
    print("===============\n......FAMOUS PERSONS.....\na.Albert Einstien\nb.Stephen Hawking\nc.Swami Vivekananda\n====================")
    speak.Speak("For which person do you want to know about?")
    person = input("Enter the requeired information(Examp-- Enter 'a' for knowing about Albert Einstien ): ")
    if person == "a":
        speak.Speak("Searching Wikipedia")
        print("Searching Wikipedia-----")
        webbrowser.open("https://en.wikipedia.org/wiki/Albert_Einstein")
    elif person == "b":
        speak.Speak("Searching Wikipedia")
        print("Searching Wikipedia-----")
        webbrowser.open("https://en.wikipedia.org/wiki/Stephen_Hawking")
        speak.Speak("Stephen William Hawking was an English theoretical physicist, cosmologist, and author who was director of research at the Centre for Theoretical Cosmology at the University of Cambridge at the time of his death. He was the Lucasian Professor of Mathematics at the University of Cambridge between 1979 and 2009.")
    elif person == "c":
        speak.Speak("Searching Wikipedia")
        print("Searching Wikipedia-----")
        webbrowser.open("https://en.wikipedia.org/wiki/Swami_Vivekananda")
        speak.Speak("Swami Vivekananda was an Indian Hindu monk. He was a chief disciple of the 19th-century Indian mystic Ramakrishna. He was a key figure in the introduction of the Indian philosophies of Vedanta and Yoga to the Western world, and is credited with raising interfaith awareness, bringing Hinduism to the status of a major world religion during the late 19th century. He was a major force in the revival of Hinduism in India, and contributed to the concept of Indian nationalism as a tool to fight against the British empire in colonial India. Vivekananda founded the Ramakrishna Math and the Ramakrishna Mission. He is perhaps best known for his speech which began with the words Sisters and brothers of America in which he introduced Hinduism at the Parliament of the World's Religions in Chicago in 1893.")
         
    else:
        speak.Speak("Wrong input")
        print("!!!!!!!!!!!!!!!!!Wrong Input!")        
elif ans == 11:
    speak.Speak("Ok " + name)
    print("Wait a few second.....")
    webbrowser.open("https://www.youtube.com/watch?v=hWPopqZJJww")   
else:
    print("!!!!!!!!!!!!!!!!!Wrong Input!")                
    




