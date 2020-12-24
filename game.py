import win32com.client as wincL

speak = wincL.Dispatch("SAPI.spVoice")

speak.Speak("Hello! Please enter your name to continue the game")
Name = input("Please Enter your name: ")
if Name == "Arnab Maity":
    speak.Speak("He is always a good boy")
else:
    speak.Speak("Please enter your gender for better game performance")
    Gender = input("Please enter your gender: ")
    speak.Speak(Name)
    speak.Speak("Please enter a number from 1 to 5")
    number = int(input("Please enter a no from (1 to 5): "))
    if number == 1 and Gender == "male":
        speak.Speak(Name)
        speak.Speak("I think You are a good boy")
    elif number == 1 and Gender == "female":
        speak.Speak(Name)
        speak.Speak("I think You are a good girl")
    elif number == 2 and Gender == "male":
        speak.Speak(Name)
        speak.Speak("I think You are a bad boy")
    elif number == 2 and Gender == "female":
        speak.Speak(Name)
        speak.Speak("I think You are a good girl")
    elif number == 3 and Gender == "male":
        speak.Speak(Name)
        speak.Speak("I think You are a good boy")
    elif number == 3 and Gender == "female":
        speak.Speak(Name)
        speak.Speak("I think You are a good girl")
    elif number == 4 and Gender == "male":
        speak.Speak(Name)
        speak.Speak("I think You are a bad boy")
    elif number == 4 and Gender == "female":
        speak.Speak(Name)
        speak.Speak("I think You are a good girl")
    elif number == 5 and Gender == "male":
        speak.Speak(Name)
        speak.Speak("I think You are a good boy")
    elif number == 5 and Gender == "female":
        speak.Speak(Name)
        speak.Speak("I think You are a good girl")
    else:
        speak.Speak("Wrong input. Program terminated")
    if 6 > number > 0:
        speak.Speak("This game is created by Arnab Maity just for fun \nDo not take it seriously")
