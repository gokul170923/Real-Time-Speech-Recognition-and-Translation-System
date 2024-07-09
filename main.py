from customtkinter import *           #gui
from tkinter import ttk

import speech_recognition as sr           #speech recognition
from googletrans import Translator        #speech translation
from gtts import gTTS                     #speak the translation



#################################################################################################

languages = (
    'Afrikaans', 'Arabic', 'Bulgarian', 'Bengali', 'Bosnian', 'Catalan', 'Czech', 'Danish', 'German', 'Greek', 
    'English', 'Spanish', 'Estonian', 'Finnish', 'French', 'Gujarati', 'Hindi', 'Croatian', 'Hungarian', 'Indonesian', 
    'Icelandic', 'Italian', 'Hebrew', 'Japanese', 'Javanese', 'Khmer', 'Kannada', 'Korean', 'Latin', 'Latvian', 
    'Malayalam', 'Marathi', 'Malay', 'Burmese', 'Nepali', 'Dutch', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 
    'Russian', 'Sinhala', 'Slovak', 'Albanian', 'Serbian', 'Sundanese', 'Swedish', 'Swahili', 'Tamil', 'Telugu', 
    'Thai', 'Filipino', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese', 'Chinese (Simplified)', 'Chinese (Mandarin/Taiwan)', 
    'Chinese (Mandarin)'
)

codes = {
    'Afrikaans': 'af','Arabic': 'ar','Bulgarian': 'bg','Bengali': 'bn','Bosnian': 'bs','Catalan': 'ca','Czech': 'cs',
    'Danish': 'da','German': 'de','Greek': 'el','English': 'en','Spanish': 'es','Estonian': 'et','Finnish': 'fi',
    'French': 'fr','Gujarati': 'gu','Hindi': 'hi','Croatian': 'hr','Hungarian': 'hu','Indonesian': 'id',
    'Icelandic': 'is','Italian': 'it','Hebrew': 'iw','Japanese': 'ja','Javanese': 'jw','Khmer': 'km','Kannada': 'kn',
    'Korean': 'ko','Latin': 'la','Latvian': 'lv','Malayalam': 'ml','Marathi': 'mr','Malay': 'ms','Burmese': 'my',
    'Nepali': 'ne','Dutch': 'nl','Norwegian': 'no','Polish': 'pl','Portuguese': 'pt','Romanian': 'ro','Russian': 'ru',
    'Sinhala': 'si','Slovak': 'sk','Albanian': 'sq','Serbian': 'sr','Sundanese': 'su','Swedish': 'sv','Swahili': 'sw',
    'Tamil': 'ta','Telugu': 'te','Thai': 'th','Filipino': 'tl','Turkish': 'tr','Ukrainian': 'uk','Urdu': 'ur',
    'Vietnamese': 'vi','Chinese (Simplified)': 'zh-CN','Chinese (Mandarin/Taiwan)': 'zh-TW','Chinese (Mandarin)': 'zh'
}

#################################################################################################

# Speech Recognition
def update_input_text(new_text):
    inputText.delete("1.0", END)
    inputText.insert("1.0", new_text)

def SpeechRecognition():
    myRecogniserClassObject = sr.Recognizer()
    currLanguage = languagesCombobox1.get()

    def listen_and_recognize():
        with sr.Microphone() as myMic:
            myAudio = myRecogniserClassObject.listen(myMic)
        try:
            myText = myRecogniserClassObject.recognize_google(myAudio, language=codes[currLanguage])
            update_input_text(myText)
        except :
            update_input_text("Couldn't recognize. Try again.")
        

    # Update text to "Start Speaking" and then start listening
    update_input_text("Start Speaking...")
    mainWindow.after(100, listen_and_recognize)

#####################################################################################################

#Translate
def update_outut_text(new_text):
    outputText.delete("1.0", END)
    outputText.insert("1.0", new_text)

def SpeechTranslate():
  mytranslator = Translator()
  currLanguage = languagesCombobox2.get()
  textToTrans = inputText.get("1.0", "end-1c")
  def translating():
      try:
          text = mytranslator.translate(textToTrans, dest=codes[currLanguage]).text
          update_outut_text(text)
      except:
          update_outut_text('Failed try again')
  update_outut_text('Translating...')
  mainWindow.after(100,translating)

#####################################################################################################

#Speek
def convert_to_speech():
    text = outputText.get("1.0", "end-1c")
    tts = gTTS(text)
    tts.save('output.mp3')
    def play():
        import pygame
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
    play()



#####################################################################################################


# GUI
mainWindow = CTk()
mainWindow.geometry("600x450")
mainWindow.title("Real-Time Speech Recognition and Translation")

mainFrame = CTkFrame(mainWindow)
mainFrame.pack(pady=20, padx=20)

####################################################################################################

# Recognize Button
buttonRecog = CTkButton(mainFrame, text="Recognize",width=10,hover_color='green',
                        command=SpeechRecognition)
buttonRecog.grid(row=0, column=2, pady=10, padx=10)


languagesCombobox1 = CTkComboBox(mainFrame,values=languages)
languagesCombobox1.set('English')
languagesCombobox1.grid(row=0,column=1,padx=10,pady=10)

####################################################################################################

# Input Label
inputLabel = CTkLabel(mainFrame, text="Input Text")
inputLabel.grid(row=0, column=0, sticky=W, padx=10, pady=10)

# Input Text Box
inputText = CTkTextbox(mainFrame, height=100)
inputText.grid(row=1, column=0, columnspan=3, padx=10)

####################################################################################################

# Translate Button
buttonTrans = CTkButton(mainFrame, text="Translate",width =10,hover_color='green'
                        ,command=SpeechTranslate)
buttonTrans.grid(row=2, column=2, pady=10, padx=10)

languagesCombobox2 = CTkComboBox(mainFrame,values=languages)
languagesCombobox2.set('English')
languagesCombobox2.grid(row=2,column=1,padx=10,pady=10)

####################################################################################################

# Output Label
outputLabel = CTkLabel(mainFrame, text="Translated Text")
outputLabel.grid(row=3, column=0, sticky=W, padx=10, pady=10)

# Output Text Box
outputText = CTkTextbox(mainFrame,height=100)
outputText.grid(row=4, column=0, columnspan=3, padx=10)

####################################################################################################

# Speak Button
buttonSpeak = CTkButton(mainFrame, text="Speak",width = 10,hover_color='green',
                        command=convert_to_speech)
buttonSpeak.grid(row=5, column=2, columnspan=2, pady=10, padx=10)

# Main loop
mainWindow.mainloop()
