import pyttsx3 # text to speech conversion lib
import datetime # to get date and time
import speech_recognition as sr  # used for speech input and recognition and convert to string
import wikipedia # use wikipedia
import webbrowser  # use web browser
import os  # for music player
import random  # use random.randint function
import smtplib  # send email 

f1=open('email_1.txt','r')  #opening sender email from file
sender_email=f1.readline()  # reading file

f2=open('email_2.txt','r')  #opening receiver email from file
receiver_email=f2.readline()  # reading file

f3=open('pass_word.txt','r')  # opening file where my password is saved
password=f3.readline()  # reading the file


engine=pyttsx3.init('sapi5')  # starting the engine of text-speech conversion
voice=engine.getProperty('voices')  # getting property of voice from engine
voice=engine.setProperty('voices',voice[0].id)  #setting property to male or female

def speak(audio):
    engine.say(audio)  # function so that engine speak
    engine.runAndWait()  # function to hear what engine speak if not then we can't hear

def wishMe():
    time=int(datetime.datetime.now().hour) # taking hour from date time
    speak("Welcome to your Personal assistance tool")
    if time>=0 and time<12:
        speak("Good Morning sir!")
    elif time>=12 and time<18:
        speak("Good AfterNoon sir!")
    elif time>=18 and time<24:
        speak("Good Evening Sir!")

    speak("I Am Your New Personal Assistance, How may i help you")

def takeCommand():
    # take speech input and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source: # making source as input from microphone
        print("Listening ......")
        r.pause_threshold=2  #seconds of non speaking audio before phrase is complete
        audio=r.listen(source) # listining from microphone

    try:
        print("Recognizing .....")
        query=r.recognize_google(audio,language='en-in') #using google web speech API to recognize the audio
        print("User said : ",query)

    except:
        print("Please say that again....")
        return "none"

    return query

def sendEmail(to,body): # simple mail transfer protocal
    speak("Sending mail to abc")
    server=smtplib.SMTP('smtp.gmail.com',587) #creating unsecure connection
    server.ehlo()
    server.starttls() #converting it to secure connection

#if you want to create secure connection from beginning use
# server=smtplib.SMTP_SSL('smtp.gmail.com',465)
# server.ehlo()

    server.login(sender_email,password) #logging in to mail
    server.sendmail(sender_email,to,body)
    server.close()



if __name__ == '__main__':
    wishMe()
    while(True):
        querry=takeCommand().lower() # taking speech to text in lower case
        
        #logic for executing task based on querry
        
        if "none" in querry:
            speak("my bad! i am not able to hear you sir,  please say louder for me")

        elif "hello how are you" in querry:
            speak("Sir i am fine!   Great to hear from you")
            
        elif "wikipedia" in querry:
            speak("Searching Wikipedia")
            querry=querry.replace("wikipedia","")
            result=wikipedia.summary(querry,sentences=2) # getting two sentences summary of wikipedia search result
            speak("According to Wikipedia ")
            print(result)
            speak(result)

        elif "open youtube" in querry:
            speak("opening youtube")
            webbrowser.open("youtube.com")  # opening youtube through web browser

        elif "open google" in querry:
            speak("opening google")
            webbrowser.open("google.com")

        elif "open stack overflow" in querry:
            speak("opening stack overflow")
            webbrowser.open("stackoverflow.com")

        elif "play music" in querry:
            speak("Playing Music")
            music_dir='F:\\My Music\\New folder'  # specifing the location
            songs=os.listdir(music_dir)  # making list of contents in location
            print(songs)
            n=random.randint(0,6) #generating random integer number
            os.startfile(os.path.join(music_dir,songs[n]))  # startfile method start the process

            #patn.join here joins path and song means pointing to the songs[n] location

        elif "the time" in querry:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")  # taking time in string
            speak(f"Sir the time is {strtime}") # to print all string and variable
            print(strtime)

        elif "the date" in querry:
            strdate=datetime.datetime.now().strftime("%d:%m:%Y")
            speak(f"Sir the date is {strdate}")
            print(strdate)

        elif "the note" in querry:
            speak("Opening notebook")
            path="C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(path)

        elif "email to abc" in querry:
            try:
                speak("What should i write?")
                body=takeCommand()
                sendEmail(receiver_email,body) # calling function declared in the top
                speak("Email has been sent!")

            except Exception as e:  # runs if error occurs anywhere before ending
                print(e)
                speak("Sorry! I am not able to sent mail")

        elif "bye bye" in querry:
            speak("Ok sir! Thank You for using me")
            speak("Bye Bye")
            speak("see you again")
            break

        else:
            speak("Sir i could not recognized your command, please instruct me again!")
