import  FRmain
import textToSpeach as tts
import ODmain
import curreny
import OCR
def doChoosedFunction ( choice ) :
    if choice=="1" or choice == "one" :
        tts.say("you have choosed face recognition")
        FRmain.main()

    if choice == "6"  :
        tts.say("you have choosed object Detection")
        ODmain.main()

    if choice == "3"  :
        tts.say("you have choosed currency Detection")
        curreny.main()
    if choice == "4"  :
        tts.say("you have choosed text reader")
        OCR.main()