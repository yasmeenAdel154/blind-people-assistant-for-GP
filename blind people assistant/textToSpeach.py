from gtts import  gTTS
import os

def say (text) :
    # Replace with the text you want to convert to speech

    """
    text = "hello , please say number of what do you want to do\n\n" \
           " say 1 - for face recognition\n\n" \
           " say 2 - for object detection\n\n" \
           " say 3 - for currency detection\n\n" \
           " say 4 - for text reader\n\n"
    """

    import pyttsx3



    # Initializes the pyttsx3 engine
    engine = pyttsx3.init()

    # Converts the text to speech
    engine.say(text)
    engine.runAndWait()


