import akinator
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS
import speech_recognition as sr

import json

bWords = json.loads(open("bWords.json", "r").read())

def takeCommand():
    r=sr.Recognizer()
    microphone=sr.Microphone()
    r.pause_threshold=0.5
    with microphone as mic: r.adjust_for_ambient_noise(mic)
    try:
        print("Listening....")
        with microphone as mic: audio=r.listen(mic)
        print("Recognizing")
        Query=r.recognize_google(audio,language='en-us')
        print("You said: ",Query)
        return Query
    except Exception as e:
        print(e)
        print("Couldn't get it, please repeat")
        return "b"

def myspeak(text):
    for bWord in bWords.keys():
        if bWord in text.lower(): text = text.replace(bWord, bWords[bWord])

        bWord = "".join(list(bWord)[0].upper()) + bWord[1:len(bWord)]
        if bWord in text: text = text.replace(bWord, bWords[bWord.lower()])

    print(text)
    tts = gTTS(text, lang="en", slow=False)
    tts.save("sound.mp3")
    # Input an existing mp3 filename
    mp3File = './sound.mp3'
    # load the file into pydub
    music = AudioSegment.from_mp3(mp3File)
    print("Playing mp3 file...")
    # play the file
    play(music)
    return True
def aki():
    aki = akinator.Akinator()
    print("here")
    q = aki.start_game()

    while aki.progression <= 80:
                spoken = myspeak(q)
                a = takeCommand().lower()
                if a == "b":
                    try:
                        q = q
                    except akinator.CantGoBackAnyFurther:
                        print("pass")
                        pass
                else:
                    try:
                        if "no" in a:
                            q = aki.answer(1)
                        elif "yes" in a:
                            q = aki.answer(0)
                        else:
                            print("Error")
                    except:
                        pass

    aki.win()

    myspeak("It's "+aki.first_guess['name']+"("+ aki.first_guess['description']+")! Was I correct?")
    print(aki.first_guess['absolute_picture_path'])
    correct = input("??")
    if correct.lower() == "yes" or correct.lower() == "y":
        print("Yay\n")
    else:
        print("Oof\n")


# def speak():
#     # Input an existing mp3 filename
#     mp3File = './sound.mp3'
#     # load the file into pydub
#     music = AudioSegment.from_mp3(mp3File)
#     print("Playing mp3 file...")
#     # play the file
#     play(music)

# speak("Hi, I'm Akinator!... I will ask you some questions & try to guess what character you are thinking about")


myspeak("Hello i am your Akinator, please think about a character")
aki()