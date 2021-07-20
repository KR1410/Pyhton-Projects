import pyttsx3 #text to speech conversion library #works offline as well
import speech_recognition as sr #used to  recognize our voice
from datetime import datetime #inbuilt module
import wikipedia #fetching information from the internet
import webbrowser #used to open websites on browser
import os #interacting with our operating system
import random
import smtplib #in built module

engine = pyttsx3.init('sapi5') #used to get voices present inside our windows
voice = engine.getProperty('voices') #two voices male and female are already present

engine.setProperty('voice',voice[1].id) #sets the voice as the female voice

#print(voices[1].id) #0 is of male and 1 is of female

def speak(speech): #function for voice assistant
    engine.say(speech) #speech,audio,line,xyz we can write anything
    engine.runAndWait() #this runs the engine.say(...)

def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning KR")
    elif hour>=12 and hour<17:
        speak("Good Afternoon KR")
    else:
        speak("Good Evening KR")

    speak("I am Friday, how may I help you")

def takecommand():
    #it takes voice input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source) #listens for the user input
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #google recognizer
        print(f"{query}\n")
        #if by chance it is unable to  recognize the voice
    except Exception as e:
        #print(e)
        print("boss! please pardon")
        speak("boss! please pardon")
        return ""
    return query
'''
def send_email(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sender_email', 'password')
    server.send('sender_email', to, content)
    server.close()
'''

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        # logic for executing tasks based on query

        if 'wikipedia' in query:
            speak("Searching in Wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            #we can also use wikipedia.search(query, results=5)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'geeks' in query:
            webbrowser.open("geeksforgeeks.org")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\KR\\Desktop\\KR\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            random_song = random.choice(songs)
            print(f"playing: {random_song}")
            os.startfile("C:\\Users\\KR\\Desktop\\KR\\Songs\\" + random_song)

        elif 'time' in query:
            time_now = datetime.now().strftime("%H: %M: %S")
            speak(f"sir the time is {time_now}")

        elif 'exit' in query:
            break
        
        else:
            speak("no results related to your query")

'''
        elif 'email' in query: #sending email to yourself
            try:
                speak("what should I send")
                content = takecommand()
                to = "kartikeyrajpoot14@gmail.com"
                send_email(to,content)
                speak("Email has been sent")
            except Exception as e:
                    print(e)
                    print("sorry unable to send email")
                    '''
