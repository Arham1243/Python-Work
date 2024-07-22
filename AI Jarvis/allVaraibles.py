# All Imports
import pyttsx3
import requests
import datetime
from datetime import date
import os
import pyaudio
import wikipedia
import pywhatkit
import time
import webbrowser
import pyautogui
# import playsound
import speech_recognition as sr

# All Global Varibles
secretFile = open("secrets/jarvisPassword.txt", "r")
password = secretFile.read()
secretFile.close()
engine = pyttsx3.init('sapi5')
engine.setProperty("rate", 210)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
currentTime = datetime.datetime.now().strftime("%H:%M")
todaydate = date.today().strftime("%d-%b-%Y")
outputPath = "C:\\\Program Files\\\Output Messenger\\OutputMessenger.exe"
portablePath = "C:\\Users\\10084\Documents\\Firefox.SalesSupport\\FirefoxPortable"
codePath = "C:\\Users\\11007\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
photoshopPath = "C:\\Program Files\Adobe\\Adobe Photoshop CC 2015\\Photoshop.exe"
xamppPath = "C:\\xampp\\xampp-control.exe"
pickerPath = "C:\\Users\\10084\\Downloads\\jcpicker_32bit.exe"
snippingToolPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\SnippingTool.exe"
