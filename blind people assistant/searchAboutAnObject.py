from gtts import  gTTS
import os
import time

def searchAboutAnObject ( searchObject , classIds , classNames ) :

    print(classIds)
    classIds = list(set(classIds))  # to get the unique values
    text = "The " + searchObject + " is not here ."
    for classId in classIds:
        if ( searchObject == classNames[classId - 1] ) :
            text = "The " + searchObject + " is here ."
            break


    #tts = gTTS(text=text, lang='en')
    #tts.save("theResultOfSearch.mp3")
    #os.system("theResultOfSearch.mp3")

    print("Start of program")
    #time.sleep(1.5)  # Wait for 5 seconds
    print("End of wait")

    print("all good")
    print(text)