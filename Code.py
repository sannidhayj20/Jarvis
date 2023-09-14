import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import keyboard
import time
import pyautogui



MASTER = 'Sunny'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
            
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>= 12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    speak("I am Jarvis at your service. How may i help you sir?")
        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        r.adjust_for_ambient_noise(source,duration= 1)
        audio =r.listen(source) 
        
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
        
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("sannidhay2004@gmail.com","Hanuman2014")
    server.sendmail("sannidhay2004@gmail.com",to,content)
    server.close()

def mailRecepient():
    x = takeCommand()
    if "1" in x:
        x = "youngcvp@gmail.com"
    if "myself" in x:
        x ="sannidhay.j.tws@treamis.org"
    if "principal" in x:
        x = "jyothis.mathew@treamis.org"
    return x

def spass():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>= 12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    print("I am your spotify assistant up and running sir")
    speak("I am your spotify assistant up and running sir")
    while True:
        spassc = takeCommand().lower() 

        if "play" in spassc:
            keyboard.press("space")
            keyboard.release("space")
        
        if "pause" in spassc:
            keyboard.press("space")
            keyboard.release("space")

        if "increase" in spassc:
            keyboard.press("ctrl")
            keyboard.press("up")
            keyboard.release("up")
            keyboard.release("ctrl")

        if "up" in spassc:
            keyboard.press("ctrl")
            keyboard.press("up")
            keyboard.release("up")
            keyboard.release("ctrl")

        if "decrease" in spassc:
            keyboard.press("ctrl")
            keyboard.press("down")
            keyboard.release("down")
            keyboard.release("ctrl")

        if "down" in spassc:
            keyboard.press("ctrl")
            keyboard.press("down")
            keyboard.release("down")
            keyboard.release("ctrl")

        if "next" in spassc:
            keyboard.press("ctrl")
            keyboard.press("right")
            keyboard.release("right")
            keyboard.release("ctrl")
            time.sleep(2)

        if "previous" in spassc:
            time.sleep(1)
            keyboard.press("ctrl")
            keyboard.press("left")
            keyboard.release("left")
            keyboard.release("ctrl")
            time.sleep(0.1)
            keyboard.press("ctrl")
            keyboard.press("left")
            keyboard.release("left")
            keyboard.release("ctrl")
        
        if "close" in spassc:
            keyboard.press("alt")
            keyboard.press("f4")
            keyboard.release("f4")
            keyboard.release("alt")
            speak("exiting spotify assitant")
            break

        if "done" in spassc:
            keyboard.press("alt")
            keyboard.press("f4")
            keyboard.release("f4")
            keyboard.release("alt")
            speak("exiting spotify assitant")
            break

        if "quit" in spassc:
            keyboard.press("alt")
            keyboard.press("f4")
            keyboard.release("f4")
            keyboard.release("alt")
            speak("exiting spotify assistant")
            break

if __name__== "__main__" :
        while True:
            query = takeCommand().lower()

            if "jarvis" in query:
                print("Initialising Jarvis...")
                speak("Initialising Jarvis...")
                wishMe()

            if "can you hear me" in query:
                speak("Yes")

            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            if "google" in query:
                query = query.replace("search","")
                query = query.replace("google","")
                query = query.replace("results","")
                query = query.replace("show","")
                query = query.replace("me","")
                query = query.replace("in","")
                query = query.replace("for","")
                speak("showing results for" + query )
                time.sleep(0.1)
                webbrowser.open("google.com")
                time.sleep(3)
                pyautogui.typewrite(query)
                keyboard.press("enter")
                keyboard.release("enter")
            
            if "youtube" in query:
                query = query.replace("search","")
                query = query.replace("youtube","")
                query = query.replace("results","")
                query = query.replace("show","")
                query = query.replace("me","")
                query = query.replace("in","")
                query = query.replace("for","")
                speak("showing results for" + query )
                time.sleep(0.1)
                webbrowser.open("youtube.com")
                time.sleep(5)
                keyboard.press('tab')
                keyboard.release('tab')
                time.sleep(0.1)
                keyboard.press('tab')
                keyboard.release('tab')
                time.sleep(0.1)
                keyboard.press('tab')
                keyboard.release('tab')
                time.sleep(0.1)
                keyboard.press('tab')
                keyboard.release('tab')
                time.sleep(0.1)
                pyautogui.typewrite(query)
                time.sleep(0.1)
                keyboard.press('enter')
                keyboard.release('enter')

            if "website" in query:
                speak("Tell me the website name")
                hg = takeCommand()
                hg = hg.replace(" ","")
                webbrowser.open(hg +".com")
            
            if 'open spotify' in query:
                speak("Opening Spotify...")
                path =('C:\\Users\\Sannidhay\\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe')
                os.startfile(path)
                speak("Initiating spotify assistant")
                spass()

            if "pause" in query:
                keyboard.press("space")
                keyboard.release("space")

            if "play" in query:
                keyboard.press("space")
                keyboard.release("space")

            if "computer" in query:
                webbrowser.open("https://meet.google.com/epz-rgmr-ckn")   
                time.sleep(7)
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("enter")
                keyboard.release("enter")
                keyboard.press("ctrl")
                keyboard.press("d")
                keyboard.release("d")
                keyboard.release("ctrl")

            if "phy" in query:
                webbrowser.open("https://meet.google.com/sxz-opha-vpf")  
                time.sleep(7)
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("enter")
                keyboard.release("enter")
                keyboard.press("ctrl")
                keyboard.press("d")
                keyboard.release("d")
                keyboard.release("ctrl")

            if "chem" in query:
                webbrowser.open("https://meet.google.com/axx-oiox-hpq")   
                time.sleep(7)
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("enter")
                keyboard.release("enter")
                keyboard.press("ctrl")
                keyboard.press("d")
                keyboard.release("d")
                keyboard.release("ctrl")

            if "math" in query:
                webbrowser.open("https://meet.google.com/rgz-fidt-dqm?classicUi=1")   
                time.sleep(7)
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("enter")
                keyboard.release("enter")
                keyboard.press("ctrl")
                keyboard.press("d")
                keyboard.release("d")
                keyboard.release("ctrl")

            if "english" in query:
                webbrowser.open("https://meet.google.com/okv-omuh-cho")   
                time.sleep(7)
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("tab")
                keyboard.release("tab")
                keyboard.press("enter")
                keyboard.release("enter")
                keyboard.press("ctrl")
                keyboard.press("d")
                keyboard.release("d")
                keyboard.release("ctrl")

            if "unmute" in query:
                speak("Warning!")
                speak("your mic is on now")
                keyboard.press("ctrl")
                keyboard.press("d")
                keyboard.release("d")
                keyboard.release("ctrl")
                gh = takeCommand()
                if 'None' in gh:
                    keyboard.press("ctrl")
                    keyboard.press("d")
                    keyboard.release("d")
                    keyboard.release("ctrl")

            if 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir the time is {strTime}")
                
            if 'open code' in query:
                path = ("C:\\Users\\Sannidhay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            
            if 'mail' in query:
                try:
                    speak("What should i say?")
                    content = takeCommand()
                    speak("whom should i send this to")
                    to = mailRecepient()
                    sendEmail(to,content)
                    speak("Email has been sent!" )
                    speak("Would u like confirmation")
                    vb = takeCommand().lower()
                    if 'yes' in vb:
                        webbrowser.open("https://mail.google.com/mail/u/2/#sent")

                                

                except Exception as e:
                    print(e)
                    speak("Sorry I wasnt able to send this email due to")
                    speak(e)

            if "whatsapp message" in query:
                webbrowser.open("https://web.whatsapp.com/")
                time.sleep(12)
                keyboard.press("tab")
                keyboard.release("tab")
                time.sleep(1)
                speak("Do u want me to search the recipient")
                d = takeCommand()
                if 'yes' in d:
                    speak("please tell me the recipient")
                    g = takeCommand()
                    pyautogui.typewrite(g)

                else:
                    keyboard.press("down")
                    keyboard.release("down")    

            if "this chat" in query:
                keyboard.press("enter")
                keyboard.release("enter")
                speak("what should i say")
                while True:
                    z= takeCommand()
                    pyautogui.typewrite(z)
                    if "spam" in z:
                        import Spammer
                        keyboard.press("enter")
                        keyboard.release("enter")

                    if 'None' in z:
                        keyboard.press("Backspace")
                        keyboard.release("Backspace")
                        keyboard.press("Backspace")
                        keyboard.release("Backspace")
                        keyboard.press("Backspace")
                        keyboard.release("Backspace")
                        keyboard.press("Backspace")
                        keyboard.release("Backspace")
                        speak("U can proceed with next command")
                        break 

                    else:
                        keyboard.press("enter")
                        keyboard.release("enter")

            if 'send another chat' in query:
                keyboard.press("tab")
                keyboard.release("tab")
                time.sleep(0.1)
                keyboard.press("tab")
                keyboard.release("tab")
                time.sleep(0.1)
                speak("would you like me to search for the recipient ")
                p = takeCommand()
                if 'yes' in p:
                    speak("please tell me the recipient")
                    a = takeCommand()
                    pyautogui.typewrite(a)

                else:
                    keyboard.press("down")
                    keyboard.release("down")

            if "gift" in query:
                webbrowser.open("https://youtu.be/V-_O7nl0Ii0")
                time.sleep(5)
                keyboard.press('f')
                keyboard.release('f')
                time.sleep(26)
                keyboard.press("space")
                keyboard.release("space")
                speak("Hahahaha... u just got rickrolled")

            if "close current tab" in query:
                speak("Closing current tab")
                keyboard.press('ctrl')
                keyboard.press('W')
                keyboard.release('W')
                keyboard.release('ctrl')

            if "first tab" in query:
                speak("switching to tab 1")
                keyboard.press("ctrl")
                keyboard.press("1")
                keyboard.release("1")
                keyboard.release("ctrl")

            if "second tab" in query:
                speak("switching to tab 2")
                keyboard.press("ctrl")
                keyboard.press("2")
                keyboard.release("2")
                keyboard.release("ctrl")

            if "third tab" in query:
                speak("switching to tab 3")
                keyboard.press("ctrl")
                keyboard.press("3")
                keyboard.release("3")
                keyboard.release("ctrl")

            if "open new tab" in query:
                speak("opening a new tab")
                keyboard.press("ctrl")
                keyboard.press("t")
                keyboard.release("t")
                keyboard.release("ctrl")  

            if "close window"  in query:
                speak("closing window")
                keyboard.press('alt')
                keyboard.press('f4')
                keyboard.release('f4')
                keyboard.release('alt')

            if "open new window" in query:
                speak("opening new window")
                keyboard.press("ctrl")
                keyboard.press("n")
                keyboard.release("n")
                keyboard.release("ctrl")

            if "open web browser" in query:
                speak("opening web browser")
                webPath =("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk")
                os.startfile(webPath)

            if "history" in query:
                speak("Clearing history...sir")
                time.sleep(1)
                keyboard.press("ctrl")
                keyboard.press("h")
                keyboard.release("h")
                keyboard.release("ctrl")
                time.sleep(1)
                keyboard.press("Tab")
                keyboard.release("Tab")
                time.sleep(0.1)
                keyboard.press("down")
                keyboard.release("down")
                time.sleep(0.1)
                keyboard.press("down")
                keyboard.release("down")
                time.sleep(0.1)
                keyboard.press("Enter")
                keyboard.release("Enter")
                time.sleep(0.1)
                keyboard.press("Tab")
                keyboard.release("Tab")
                time.sleep(0.1)
                keyboard.press("Tab")
                keyboard.release("Tab")
                time.sleep(0.1)
                keyboard.press("Tab")
                keyboard.release("Tab")
                time.sleep(0.1)
                keyboard.press("Tab")
                keyboard.release("Tab")
                time.sleep(0.1)
                keyboard.press("Tab")
                keyboard.release("Tab")
                time.sleep(0.1)
                keyboard.press("Tab")
                keyboard.release("Tab")
                time.sleep(0.1)
                keyboard.press("Tab")
                keyboard.release("Tab")
                time.sleep(0.1)
                keyboard.press("Tab")
                keyboard.release("Tab")
                time.sleep(0.1)
                keyboard.press("Tab")
                keyboard.release("Tab")
                time.sleep(0.1)
                keyboard.press("Tab")
                keyboard.release("Tab")
                time.sleep(0.1)
                keyboard.press("Tab")
                keyboard.release("Tab")
                time.sleep(0.1)
                keyboard.press("Tab")
                keyboard.release("Tab")
                time.sleep(0.1) 
                keyboard.press("Tab")
                keyboard.release("Tab")
                time.sleep(0.1)
                keyboard.press("Enter")
                keyboard.release("Enter")

                
                                

            if "weather" in query:
                import requests
                query = query.replace("show","")
                query = query.replace("me","")
                query = query.replace("the","")
                query = query.replace("weather","")
                query = query.replace("reports","")
                query = query.replace("report","")
                query = query.replace("for","")
                query = query.replace("of","")
                query = query.replace("today","")
                query = query.replace("tommorow","")
                query = query.replace("wear","")
                query = query.replace(" ","")
                print(query)
                print('Displaying weather report for: ' + query)
                url = 'https://wttr.in/{}'.format(query)
                res = requests.get(url)
                print(res.text)
                
            if "spam" in query:
                import Spammer
                keyboard.press("enter")
                keyboard.release("enter")

            if "switch tab" in query:
                keyboard.press('alt')
                keyboard.press('tab')
                keyboard.release('tab')
                keyboard.release('alt')

            if "thank you" in query:
                speak("Thats very sweet of you sir")
        
            if "down" in query:
                keyboard.press("down")
                keyboard.release("down")

            if "minimise" in query:
                keyboard.press("win")
                keyboard.press('down')
                keyboard.release('down')
                keyboard.release('win')
                time.sleep(0.1)
                keyboard.press('win')
                keyboard.press('down')
                keyboard.release('down')
                keyboard.release('win')

            if 'desktop' in query:
                keyboard.press('win')
                keyboard.press('m')
                keyboard.release('m')
                keyboard.release('win')

            if 'full screen' in query:
                keyboard.press('win')
                keyboard.press('up')
                keyboard.release('up')
                keyboard.release('win')

            if "up" in query:
                keyboard.press("up")
                keyboard.release("up")

            if 'death' in query:
                webbrowser.open('https://www.youtube.com/watch?v=TWB31WFomz4&t=35s')
                time.sleep(2)
                keyboard.press("f")
                keyboard.release("f")


            if "outside" in query:
                from bs4 import BeautifulSoup
                import requests
                from Jarvis import speak
                search = "temprature in chennai"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                print(f"current {search} is {temp}")
                speak("Sir")
                speak(f"current {search} outside is {temp}")

            if 'shut down' in query:
                keyboard.press("win")
                keyboard.press("m")
                time.sleep(0.1)
                keyboard.press("win")
                keyboard.press("alt")
                keyboard.press("f4")
                keyboard.release("f4")
                keyboard.release("alt")
                keyboard.release("win")
                time.sleep(0.1)
                keyboard.press("enter")
                keyboard.release("enter")

            if 'shutdown' in query:
                keyboard.press("win")
                keyboard.press("m")
                time.sleep(0.1)
                keyboard.press("win")
                keyboard.press("alt")
                keyboard.press("f4")
                keyboard.release("f4")
                keyboard.release("alt")
                keyboard.release("win")
                time.sleep(0.1)
                keyboard.press("enter")
                keyboard.release("enter")

            if "all tabs" in query:
                keyboard.press('win')
                keyboard.press('tab')
                keyboard.release('tab')
                keyboard.release('win')

            if "left" in query:
                keyboard.press("left")
                keyboard.release("left")

            if "right" in query:
                keyboard.press("right")
                keyboard.release("right")

            if "this one" in query:
                keyboard.press("enter")
                keyboard.release("enter")

            if "horn" in query:
                print("I am very horny too sir")
                speak("I am very horny sir")
                speak("hahahhahahahahahahahahahahah")

            if "*" in query:
                speak("watch your language")

            if "bright" in query:
                import SBCP

            if "quit" in query:

                speak("Sir,before I quit could I tell you something")
                b = takeCommand()
                if "y" in b:
                    import Iloveyou
                    speak("I am quitting..., have a good day ahead sir")
                    quit()

                if "sure" in b:
                    import Iloveyou
                    speak("I am quitting..., have a good day ahead sir")
                    quit()

                if "k" in b:
                    import Iloveyou
                    speak("I am quitting..., have a good day ahead sir")
                    quit()
                

                else:
                    speak("Ouch thats ok sir")
                    speak("goodbye sir")       
                    quit()     
        

            if "amazon" in query:
                import AmazonTracker

                
