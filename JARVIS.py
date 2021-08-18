import pyttsx3

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[7].id)

engine.say("Hello, this is a test" )
engine.runAndWait()