import ppttsx3

engine = ppttsx3.init('sapi5')
voices = engine.getproperty('voices')
engine.setproperty('voice',voices[0].id)





def speak(audio):
    engine.say(audio)
    engine.runandwait()
if  __name__=="main":
    speak("harry is a good boy")    

    

    