import pyttsx3

def speak(audio):
    voiceEngine = pyttsx3.init()

    rate = voiceEngine.getProperty('rate')
    volume = voiceEngine.getProperty('volume')
    voice = voiceEngine.getProperty('voice')

    newVoiceRate = 110

    newVolume = 0.20
    voiceEngine.setProperty('rate', newVoiceRate)
    voiceEngine.say(audio)
    voiceEngine.runAndWait()


speak("hello world")