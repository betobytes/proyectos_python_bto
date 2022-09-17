import speech_recognition as sr 
import pyttsx3

name = friday 
listener = sr.Recognizer()

engine = pyttsx3.init()
 
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
	engine.say(text)
	engine.runAndWait()

def listen():
 try:
     with sr.Microphone() as source:
    	 print("escuchando-----")
    	 voice = listener.listen(source)
    	 rec = listener.recognize_google(voice)
    	 rec = rec.lower()
    	 if name in rec: 
    		 rec = rec.replace(name,'')
    		 talk(rec)

    	 #print(rec)

 except:
	 pass  

# las acciones para seguir 
def run():
	rec = listen() 

	if 'reproduce' in rec:
		talk(rec)
		print('play')

run()
