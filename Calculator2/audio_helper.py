import pyttsx3

class PlayAudio:
    def __init__(self,voice="female",speakstatus=True):
        self.voice = "female"
        self.speakstatus = speakstatus
        self.speakwords = {
            '1':'one',
            '2':'two',
            '3':'three',
            '4':'four',
            '+':'plus',
            '=':'equal to'
        }
        self.engine = pyttsx3.init()
        v = self.engine.getProperty('voices')
        self.engine.setProperty('voice',v[1].id)

    def speak(self,content):
        if self.speakstatus==True:
            self.engine.say(self.speakwords[content])
            self.engine.runAndWait()

