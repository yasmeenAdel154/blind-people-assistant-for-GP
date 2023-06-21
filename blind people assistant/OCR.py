import cv2 as cv
import os
import pytesseract
import pyttsx3
import flask
from flask import Flask, jsonify, request

import pyttsx3

# Initializes the pyttsx3 engine
engine = pyttsx3.init()

#os.chdir(r"D:\\Ocr")
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
app = Flask(__name__)


def prepare_image(img):
    # img = cv.imread(img)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 85, 11)
    return threshold


def ocr(threshold):
    text = pytesseract.image_to_string(threshold)
    return text


@app.route("/predict", methods=["POST"])
def infer_image():
    file = request.files.get('file')
    print(file)

    if not file:
        return

    img2 = cv.imread(file.filename)
    image = prepare_image(img2)

    return jsonify(result=ocr(image))


@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Inference'


# engine = pyttsx3.init()
# voice = engine.getProperty('voices')
# #voice[0] is male
# #voice[1] is female
# engine.setProperty('voice', voice[1].id)
# engine.setProperty('rate', 130)
# photo = cv.imread("C:/Users/abdel/PycharmProjects/pythonProject1/myImg.png")
# image = prepare_image(photo)
# print(ocr(image))
# engine.say(ocr(image))
# engine.runAndWait()
# engine.stop()

#if __name__ == '__main__':
    #app.run(debug=True)

def main () :
    img2 = cv.imread("OCRtest.jpg")

    from PIL import Image

    # Open the image file
    image = Image.open('OCRtest.jpg')
    engine.say("please take the photo of the book ")
    engine.runAndWait()
    # Show the image
    image.show()

    image = prepare_image(img2)

    result=ocr(image)


    engine.say(result)
    engine.runAndWait()


