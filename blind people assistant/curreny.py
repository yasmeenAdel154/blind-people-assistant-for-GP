import torch
import numpy as np
import cv2

import pyttsx3

def main () :
    # Initializes the pyttsx3 engine
    engine = pyttsx3.init()

    model = torch.hub.load('yolov5', 'custom', path='best.pt', source='local')  # local model
    img = 'test3.jpeg'

    text = "please take your photo "
    engine.say(text)
    engine.runAndWait()

    results = model(img)
    results.show()

    def convertResultToArray(results) :
        results = results.pandas().xyxy[0].to_dict(orient="index")
        print(results)
        data = results.values()
        array = list(data)
        arr = np.array(array)
        n = len(arr)

        return arr , n

    arr , n = convertResultToArray(results)
    print(int(arr[0].get("name").strip("pounds m")))
    mylist = []


    def creatingarr(arr,n):
        for i in range(n):
            x = arr[i].get("name").strip("pounds m new")
            print(x)
            mylist.append(float(x))
        return mylist


    def countDic(mylist):
        mp = dict()
        ans = 0
        for i in range(len(mylist)):
            ans+=mylist[i]
            if mylist[i] in mp.keys():
                mp[mylist[i]] += 1
            else:
                mp[mylist[i]] = 1
        return ans


    print(creatingarr(arr,n))
    text = countDic(mylist)
    print(text)




    # Converts the text to speech
    engine.say(text)
    engine.runAndWait()
