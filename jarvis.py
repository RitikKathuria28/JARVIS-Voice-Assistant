import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am jarvis sir. How can I help you")            


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecmd():
    '''
    It takes mirophone input from the user and return the string output
    '''    
    s = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        s.pause_threshold = 1.1
        aud = s.listen(source)

    try:
        print("Recognizing...")
        query = s.recognize_google(aud, language='en-in')
        print(f"You said {query}")  
        
    except Exception as e:
        print(e)
        print("Please say it again")
        return "None"    
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')    # Pls enter your email and password here
    server.sendmail('youremail@gmail.com', to, content)
    server.close()    

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecmd().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "") # it replace wikipedia word in query with blank as we dont want to search wikipedia on wikipedia
            results = wikipedia.summary(query, sentences=2)  # this will get search results from wikipedia by using query and return only two sentences
            speak('According to wikipedia...')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

               

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open primevedio' in query:
            webbrowser.open("primevedio.com")    

        elif 'play music' in query:
            music_dir = 'C:\\Users\\ritik\\Desktop\\jarvis in python\\songs'
            songs = os.listdir(music_dir)
            ls = []
            for i in range(len(songs)):
                ls.append(i)
            ran_song = random.choice(ls)    
            os.startfile(os.path.join(music_dir, songs[ran_song]))

            # play a randon song everytime from the the directory


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ritik\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)    


        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ritikyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email") 

        elif 'exit' in query:
            speak("Thankyou sir Have a nice day")   
            break                 