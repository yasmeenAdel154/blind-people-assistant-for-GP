import speech_recognition as sr
import textToSpeach as bs
import doChoosedFunction as dcf

import pyttsx3
text = "hello , please say number of what do you want to do\n\n" \
           " say 1 - for face recognition\n\n" \
           " say 6 - for object detection\n\n" \
           " say 3 - for currency detection\n\n" \
           " say 4 - for text reader\n\n"

print(text)
bs.say(text)
def main () :

    r = sr.Recognizer()

    with sr.Microphone() as source :
        r.adjust_for_ambient_noise(source)

        print("Please say something")
        text = "Please say something"
        bs.say(text)

        audio = r.listen(source)

        print("Recognizing Now .... ")

        # recognize speech using google

        try:
            choice =  r.recognize_google(audio)
            print("You have said \n" +choice)
            if ( choice!="1" and choice != "6" and choice != "3" and choice != "4" ) :
                main()
            else :
                dcf.doChoosedFunction(choice)
                # write audio
                with open("recorded.wav", "wb") as f:
                    f.write(audio.get_wav_data())
                print("Audio Recorded Successfully \n ")


        except Exception as e:
            print("Error :  " + str(e))
            main()
    #cf.call_function(choice)



if __name__ == "__main__":
    main()

