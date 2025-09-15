import pyttsx3
engine = pyttsx3.init()

# Change the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female (may vary by system)

engine.say("Hi I am Arya, your Virtual Assistant")
engine.runAndWait()