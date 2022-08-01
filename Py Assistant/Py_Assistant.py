from datetime import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
#import pyjokes
import pyautogui



global listening_mode   
listening_mode = False#Set to True for Debugging
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening.....')
            listener.adjust_for_ambient_noise(source, duration=2)
            voice = listener.listen(source)
            print('Processing Speech to Text')
            command = listener.recognize_google(voice)
            command = command.lower()
            print('Audio: ' + command)
            return command
                
    #Catch not Speech noise error
    except sr.UnknownValueError:
        print('UnknownValueError')
    except sr.RequestError as e:
        print("pyttsx3 error; {0}".format(e))
    
def run_alexa():
    command = take_command()
    if(not listening_mode):
        if(iscalled(command, 'alexa')):#name of your assistant here/ Always check if the name that your calling is the same
            command = trycut(command, 'alexa')#remove the name before interpreting
            interpret(command)
        else:
            print('Not Called')
        
    else:
        #print('else')
        interpret(command)

def iscalled(command, name):#check if called with exception if none
    try:
        if name in command:
            return True
    except:
        pass
        #print('pass at iscalled');
        return False

def trycut(string, keyword):#method for revoming keyboard with exception if none/ if string does not contain the keyboard string will just be return
    try:
        string = string.replace(keyword, '')
    except:
        pass
        #print('pass at trycut');
    return string

keywords = ['listening mode', 'stanby mode', 'youtube', 'time', 'wiki', 'help', 'mouse']
def interpret(command):
    global listening_mode  
    command = trycut(command, 'alexa')
    print('Processing Text to Speech')
    try:
        print('Command: ' + command)#print the final string to check for keyword command
        #if 'listening mode' in command:
        if keywords[0] in command:
            listening_mode = True
            print('listening mode')
            #talk('listening mode')
            talk('Set to listening mode for debugging')   
        elif 'stanby' in command:
        #elif keywords[1] in command:
           listening_mode = False
           print('stanby mode')
           talk('stanby mode')
        #elif 'youtube' in command:
        elif keywords[2] in command:
            yt = command.replace('youtube', '')
            talk('playing' + yt)
            print(command)
            pywhatkit.playonyt(yt)
        #elif 'time' in command:
        elif keywords[3] in command:
            time = datetime.now().strftime('%H:%M %p')
            talk('The current time is ' + time)
        #elif 'wiki' in command:
        elif keywords[4] in command:
            person = command.replace('wiki', '')
            info = wikipedia.summary(person, 1) 
            print(info)
            talk(info)
        #elif 'joke' in command:
        #    talk(pyjokes.getjoke())
        #elif 'help' in command:
        elif keywords[5] in command:
            #talk('hi as of ' + datetime.now() + ' i have ' + len(keywords) + ' commands and these are ' )
            talk('hi as of today i have ' + str(len(keywords)) + ' commands and these are ' )
            speakarray(keywords)
        elif keywords[6] in command:
            loc = command.split(' ')
            print('Moving mouse to ' + str(loc[1]) + ' by ' + str(loc[2]))
            Mouse(loc[1], loc[2])
            print(pyautogui.position())
        else:
            talk('cant understand, say it again')
        print('listening_mode: ' + str(listening_mode))
    except TypeError:
        #talk('cant understand, say it again') 
        print('Noise or TypeError')

def speakarray(arrays):
    for rays in arrays:
        talk(rays)

def Mouse(x, y):
    pyautogui.moveRel(int(x), int(y))
    #pyautogui.click(100, 100)

def showgrid():
    print('Showing grid lines')
    #override screen and display objects python

def main():#Execute commands on startup    
    if(listening_mode):
        #talk('Set to listening mode for debugging')     
        #talk('hi as of today i have ' + str(len(keywords)) + ' commands and these are ' )
        #for word in keywords:
        #    print(word)

        #Mouse(200, 200)
        print(pyautogui.position())
main()  

while True:#RUN Forever
    run_alexa()

