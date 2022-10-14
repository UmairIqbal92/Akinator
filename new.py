#!/usr/bin/env python3
from pydub import AudioSegment
from pydub.playback import play

# Input an existing mp3 filename
mp3File = './sound.mp3'
# load the file into pydub
music = AudioSegment.from_mp3(mp3File)
print("Playing mp3 file...")
# play the file
play(music)