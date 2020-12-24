import win32com.client as wincL
import datetime

speak = wincL.Dispatch("SAPI.spVoice")

st = (("Bengali", 80), ("English", 85), ("Mathematics", 90), ("Physics", 67), ("Life science", 77), ("History", 91),
      ("Geography", 81))

hour = int(datetime.datetime.now().hour)
if 0 <= hour < 12:
    speak.Speak("Good morning")
elif 12 <= hour < 18:
    speak.Speak("Good afternoon")
else:
    speak.Speak("Good evening")
print("Time:", datetime.datetime.now())
speak.Speak("Welcome to Arnab's System")
speak.Speak("My name is Jarvis and I am the virtual assistance of Arnab")
speak.Speak("Do you want to see Arnab's details")
ans = input("Do you want to see Arnab's details: ")
if ans == "yes":
    speak.Speak("Ok You need to enter the right password to see Arnab's details")
    Password = input("Enter password to continue: ")
    if Password == "arnabmaity":
        speak.Speak("Please enter your name")
        Name = input("Please enter your name: ")
        if Name == "Arnab Maity":
            speak.Speak("Welcome back Sir")
        else:
            speak.Speak("Welcome")
            speak.Speak(Name)
            speak.Speak("You can see Arnab's details")
    else:
        print('Wrong Password!!!!!!\n Program Terminated------------')
        speak.Speak("Sorry i think you are a imposter")
else:
    speak.Speak("Ok sir! Good bye! Have a nice day")
if ans == "y" and Password == "arnabmaity":
    print('Arnab\'s Contact details')
    print("Name: Arnab Maity\nPh no: 8348132802\nAddress: Bakshi, Bagnan, Howrah\nFather's Name: Bimal"
          "Maity\nMother's Name: Uma Maity\nAge=16")
    speak.Speak("Name: Arnab Maity\nPhone Number: 8348132802\nAddress: Bakshi, Bagnan, Howrah\nFather's Name: Bimal "
                "Maity\nMother's Name: Uma Maity\nAge: 16")
    speak.Speak("Thank you for visiting our System")
    speak.Speak("Have a nice day")
