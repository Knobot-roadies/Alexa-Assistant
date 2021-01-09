import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib

# print("initailizing jarvis")

MASTER = "Pradipta"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


# this function will speak /or will wish you as per current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!" + MASTER)

    elif hour >= 12 and hour < 18:
        speak("Good afternoon" + MASTER)

    else:
        speak("good evening" + MASTER)

    speak("I am Alexa..... How may i help you?")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@gmail.com', 'password')
    server.sendmail('yourmail.com', to, content)
    server.close()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        audio = r.listen(source)

    try:
        print("recognising..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query = None
    return query


def main():
    speak("initailizing alexa......")
    wishMe()
    takecommand()
    query = takecommand()

    # logic for executing basix tasks as far teh query
    if 'wikipedia' in query.lower():
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        # webbrowser.open("youtube.com")
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    

    elif 'open gmail' in query.lower():
        url = "gmail.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'what is your name' in query.lower():
        speak('I’m shy, please come say hi..')

    elif 'play music' in query.lower():
        speak('playing music...')
        songs_dir = "C:\\Users\\KIIT\\Music"  # I have usen my directory you plese use your directory otherwise it will note open
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'exit alexa' in query.lower():
        speak('Thank you for your time,have a nice day ahead...')

    elif 'open code' in query.lower():
        codePath = "C:\Program Files\Sublime Text 3"
        os.startfile(codePath)

    elif 'email to samrat' in query.lower():
        try:
            speak("what should i sent..")
            content = takecommand()
            to = "samratchoudhury.apd@gmail.com"
            sendEmail(to, content)
            speak("email has been sent successfully...")
        except Exception as e:
            print(e)


    elif 'hi Alexa' in query.lower():
        speak("hey...what can i do for you...")


    else:
        speak("sorry i couldn't get you,please try again..")


main()
