import speech_recognition as sr 
''' Pythons default libray for speech recognition
    -easy to use and supports pyaudio
    -include multiple api's and model like google , bing
    -no cloud service account needed
    -multilingual
    -alternatives -> 
                    Google Cloud Speech-to-Text
                    Azure Speech Service
                    Vosk ( open source / multiple languages)
                    Wisper ( open sourced by open AI)
'''
  

from googletrans import Translator
''' Free Translation api provided by google
    -alternatives ->
                   DeepL API
                   Microsoft Azure Translator Text
                   Amazon Translate
'''

from gtts import gTTS
''' Free , accurate , multilingual api provided by google
    -alternatives ->
                    pyttsx3 ( offline)

'''
import pygame
''' personal prefrence
   -alternative ->
                  pydub,pyaudio,simpleaudio
'''


def SpeechRecognition():
  #instantiate the Recogniser class ( interfaces the audio input with api calls)
  myRecogniserClassObject = sr.Recognizer()

  # listening
  with sr.Microphone() as myMic:
    #this uses pyaudio under 
    print("Start Speaking")
    myAudio = myRecogniserClassObject.listen(myMic)

  # recognition (call to google api for recognisation) 
  try:
    myText = myRecogniserClassObject.recognize_google(myAudio,language="auto")
    print(myText)
  except:
    print("Couldn't recognise speek again")


def SpeechTranslate(mytext):
  #instantiate the translator
  mytranslator = Translator()

  #call the methord
  text = mytranslator.translate(mytext, dest='ko').text
  print(text)



def convert_to_speech(text):
    # call the google-text-to-speech api
    tts = gTTS(text)
    tts.save('output.mp3')
      # Initialize pygame mixer
    pygame.mixer.init()
      # Loading the generated audio
    pygame.mixer.music.load("output.mp3")
      
      # start Playing the audio file
    pygame.mixer.music.play()
      
      # and keep it running until it finishes
    while pygame.mixer.music.get_busy():
          pygame.time.Clock().tick(10)
      # release the audio else will not be able to be modified again
    pygame.mixer.music.stop()
    pygame.mixer.quit()

