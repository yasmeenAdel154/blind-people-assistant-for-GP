from gtts import  gTTS
import os
import textToSpeach as tts
def listenNamesOfClasses(classIds , classNames) :

    print(classIds)
    classIds = list(set(classIds)) # to get the unique values
    text = ""
    for classId in classIds :
        if text == "" :
            text = classNames[classId-1]
            continue
        text= text + " and " + classNames[classId-1]

        """
        tts = gTTS(text=text, lang='en')
            tts.save("test.mp3")
            os.system("test.mp3")
        """

    tts.say(text)
    print("all good")
    print(text)