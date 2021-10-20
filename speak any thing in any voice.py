import pyttsx3
a = input('Please enter the text to be said: ')
b = input('Enter in whose voice it will say (press F for female and M for male)')
if b == 'M':
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(a)
    engine.runAndWait()
if b == 'F':
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(a)
    engine.runAndWait()
else:
    print('')


