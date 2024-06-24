from gtts import gTTS 
import os

text="Hello world!"

tts= gTTS(text)

tts.save('helloworld.mp3')