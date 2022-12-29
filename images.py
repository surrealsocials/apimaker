import openai
import os
import shutil
import cv2
import time
from flask import Flask,render_template
from io import BytesIO
from PIL import Image
import wget
import requests

loading='wheel.gif'
openai.api_key = "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"
cwd=os.getcwd()

def getstory():
    url = "https://shortstories-api.onrender.com/"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return(response.json()['story'])

def sum4kids(story):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Summarize this for a second-grade student:\n\n"+story,
        temperature=0.9,
        max_tokens=164,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
    return response["choices"][0]['text']

def resize():
    # Read the image file from disk and resize it
    image = Image.open("image.png")
    width, height = 256, 256
    image = image.resize((width, height))

    # Convert the image to a BytesIO object
    byte_stream = BytesIO()
    image.save(byte_stream, format='PNG')
    byte_array = byte_stream.getvalue()

    response = openai.Image.create_variation(
      image=byte_array,
      n=1,
      size="512x512")

def memimage():
    # This is the BytesIO object that contains your image data
    byte_stream: BytesIO = [open('tempy.png','rb')]
    byte_array = byte_stream.getvalue()
    response = openai.Image.create_variation(
      image=byte_array,
      n=1,
      size="512x512"
    )
    return response

def getimage(txt):
    response = openai.Image.create(
      prompt=txt,
      n=1,
      size="512x512"
    )
    image_url = response['data'][0]['url']
    img = wget.download(image_url)
    #print('Image Successfully Downloaded: ', img)
    shutil.copyfile(img, 'tempy.png')
    
    print(img)
    return(img)

def getimageurl(txt):
    response = openai.Image.create(
      prompt=txt,
      n=1,
      size="512x512"
    )
    image_url = response['data'][0]['url']
    return (image_url)


def variation(img):
    img='tempy.png'
    response = openai.Image.create_variation(
        image=open(img, "rb"),
        n=1,
        size="512x512"
        )
    newimg = response['data'][0]['url']
    with open(img[:-4]+'v'+'.png','w') as img2:
        img2.write(newimg)

    return(newimg)

def edits(txt):
    img='tempy.png'
    response = openai.Image.create_edit(
        image=open("tempy.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt=txt,
        n=1,
        size="512x512"
        )
    newimg = response['data'][0]['url']
    with open(img[:-4]+'v'+'.png','w') as img2:
        img2.write(newimg)

    return(newimg)

