from gtts import  gTTS
import os
import textToSpeach as tts
def listenNamesOfPeople( facesNames ):

    print(facesNames)
    text = ""
    if len(facesNames) != 0 :
        for i in facesNames :
            if text == "" :
                text = i
                continue
            text= text + " and " + i

        """tts = gTTS(text=text, lang='en' )
        tts.save("test.mp3")
        os.system("test.mp3")
        import time
        print("Start of program")
        time.sleep(2)  # Wait for 5 seconds
        print("End of wait")
        """
        tts.say(text)
    print("all good")

