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
import shutil
import speech_recognition as sr
from allVaraibles import secretFile, password, engine, voices, currentTime, todaydate, outputPath, portablePath, codePath, photoshopPath, xamppPath, pickerPath, pickerPath


engine.setProperty("rate", 230)
engine.setProperty('voices', voices[1].id)


# Funtion for speak

def speak(audio):
    """This function for speak"""
    engine.say(audio)
    engine.runAndWait()


def output():
    """This funtion is for opening output"""
    speak("opening sir")
    from jarvis import outputPath
    os.startfile(outputPath)

# Function for wish me according to time


def wishMe():
    """This funtion is for wish me according to time"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        print("Good AfterNoon!")
        speak("Good AfterNoon!")
    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("How May I Help You Sir")
    speak("How May I Help You Sir")


# Function for listening user voice


def takeCommand():
    """This funtion for taking commond from user"""
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query
    except:
        speak("sorry sir, there is something wrong")


# Function for search user voice
def takeCommandSearch():
    """This funtion for taking commond from user"""
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
            query = r.recognize_google(audio, language='en-in')
        return query
    except:
        speak("sorry sir, there is something wrong")
    """This funtion for taking commond from user"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language='en-in')
    return query


# Funtions for perfoming tasks


def restart():
    """This funtion is for restart the computer"""
    try:
        speak("ok sir i am going to restart the computer")
        os.system("shutdown /r")
    except:
        speak("sorry sir, for some reason i can't shutdown the system")


def shutdown():
    """This funtion is for shutdown the computer"""
    try:
        speak("ok sir i am going to shutdown the computer")
        os.system("shutdown /s")
    except:
        speak("sorry sir, for some reason i can't shutdown the system")


def lock():
    """This funtion is for lock the computer"""
    try:
        speak("ok sir i am going to lock the computer")
        os.system("shutdown /l")
    except:
        speak("sorry sir, for some reason i can't lock the system")


def closeProgram():
    """This funtion is for close the program"""
    speak("ok sir i am closing the program")
    exit()


def youtube():
    """This funtion is for opening youtube"""
    try:
        speak("opening sir")
        webbrowser.open("www.youtube.com")
    except:
        speak("sorry sir, for some reason i can't open this")


def liveServer():
    """This funtion is for opening live server in vs code"""
    try:
        speak("opening sir")
        pyautogui.hotkey("alt", "l", "o")
    except:
        speak("sorry sir, for some reason i can't open this")


def google():
    """This funtion is for opening google"""
    try:
        speak("opening sir")
        webbrowser.open("www.goolge.com")
    except:
        speak("sorry sir, for some reason i can't open this")


def mySheet():
    """This funtion is for opening my task sheet"""
    try:
        speak("opening sir")
        webbrowser.open(
            "https://docs.google.com/spreadsheets/d/1li-RJuRX2RCbU2VJPOqwH5ir5XZ4HpRMn5ADknP-iXg/edit?pli=1#gid=65167384")
    except:
        speak("sorry sir, for some reason i can't open this")


def searchInGoogle():
    """This funtion is for search in google"""
    try:
        speak("what should i search")
        print("what should i search")
        content = takeCommandSearch()
        webbrowser.open("www.goolge.com")
        time.sleep(1)
        pyautogui.write(content, interval=0.03)
        pyautogui.hotkey("enter")
    except Exception as i:
        speak("sorry sir, for some reason i can't search")


def searchInPortable():
    """This funtion is for search in firefox portable"""
    try:
        speak("what should i search")
        print("what should i search")
        content = takeCommandSearch()
        from jarvis import portablePath
        os.startfile(portablePath)
        time.sleep(2)
        pyautogui.write(content, interval=0.03)
        pyautogui.hotkey("enter")
    except:
        speak("sorry sir, for some reason i can't search")


def openFirefox():
    """This funtion is for opening firefox"""
    try:
        speak("opening sir")
        move = pyautogui.locateOnScreen("images/firefox-tab-img.PNG")
        editBut = pyautogui.center(move)
        pyautogui.moveTo(editBut)
        pyautogui.click()
    except:
        speak("sorry sir, for some reason i can't open this")


def firefoxPortable():
    """This funtion is for opening firefox portable"""
    try:
        speak("opening sir")
        from jarvis import portablePath
        os.startfile(portablePath)
    except:
        speak("sorry sir, for some reason i can't open this")


def switchWindow():
    """This funtion is for switching window"""
    speak("ok sir")
    pyautogui.hotkey("alt", "tab")


def closeTab():
    """This funtion is for closing tabs"""
    speak("ok sir")
    pyautogui.hotkey("ctrl", "w")


def reopenTheTab():
    """This funtion is for reopen tabs"""
    try:
        speak("ok sir")
        pyautogui.hotkey("ctrl", "shift", "t")
    except:
        speak("sorry sir, for some reason i can't reopen this")


def closeWindow():
    """This funtion is for switching window"""
    speak("ok sir")
    pyautogui.hotkey("alt", "f4")


def fontAwesome():
    """This funtion is for opening font Awesome"""
    try:
        speak("opening sir")
        webbrowser.open("www.fontawesome.com")
    except:
        speak("sorry sir, for some reason i can't open this")


def boxIcon():
    """This funtion is for opening box icon"""
    try:
        speak("opening sir")
        webbrowser.open("www.boxicons.com")
    except:
        speak("sorry sir, for some reason i can't open this")


def currentTimeFunc():
    """This funtion is for knowing time"""
    try:
        from jarvis import currentTime
        currentTime
        print(f"Sir the time is {currentTime}")
        speak(f"Sir the time is {currentTime}")
    except:
        speak("sorry sir, for some reason i can't tell you time")


def todayDateFunc():
    """This funtion is for knowing date"""
    try:
        from jarvis import todaydate
        todaydate
        print(f"Sir the date is {todaydate}")
        speak(f"Sir the date is {todaydate}")
    except:
        speak("sorry sir, for some reason i can't tell you date")


def yandex():
    """This funtion is for opening yandex"""
    try:
        speak("opening sir")
        webbrowser.open("www.yandex.com")
    except:
        speak("sorry sir, for some reason i can't open this")


def vsCode():
    """This funtion is for opening vs code"""
    try:
        speak("opening sir")
        from jarvis import codePath
        os.startfile(codePath)
    except:
        speak("sorry sir, for some reason i can't open this")


def fullWindow():
    """This funtion is for doing maximize the window"""
    speak("ok sir")
    pyautogui.hotkey("win", "up")


def photoshop():
    """This funtion is for opening photoshop"""
    try:
        speak("opening sir")
        from jarvis import photoshopPath
        os.startfile(photoshopPath)
    except:
        speak("sorry sir, for some reason i can't open this")


def passwordChange():
    """This funtion is for changing the password of ai"""
    try:
        print("tell a current password")
        speak("tell a current password")
        secretFile = open("secrets/jarvisPassword.txt", "r")
        password = secretFile.read()
        secretFile.close()
        currentPassword = takeCommand().lower()
        if currentPassword == password:
            print("what password do you want")
            speak("what password do you want")
            newPassword = takeCommand().lower()
            secretFile = open("secrets/jarvisPassword.txt", "w")
            secretFile.write(newPassword)
            secretFile.close()
            print("the password is succesfully changed")
            speak("the password is succesfully changed")
        else:
            print("the password is wrong")
            speak("the password is wrong")
    except:
        speak("sorry sir, right now i cant't change the password")


def xampp():
    """This funtion is for opening xampp"""
    try:
        speak("opening sir")
        from jarvis import xamppPath
        os.startfile(xamppPath)
    except:
        speak("sorry sir, for some reason i can't open this")


def colourPicker():
    """This funtion is for opening colour picker"""
    try:
        speak("opening sir")
        from jarvis import pickerPath
        os.startfile(pickerPath)
    except:
        speak("sorry sir, for some reason i can't open this")


def outlook():
    """This funtion is for opening outlook"""
    try:
        speak("opening sir")
        pyautogui.hotkey("ctrl", "alt", "o")
    except:
        speak("sorry sir, for some reason i can't open this")


def typeIt():
    """This funtion is for typing"""
    try:
        speak("ok sir")
        content = takeCommandSearch()
        pyautogui.write(content, interval=0.03)
    except:
        speak("sorry sir, for some error i can't type")


def enter():
    """This funtion is for hitting enter"""
    pyautogui.hotkey("enter")


def currentPassword():
    """This funtion is for knowing current password"""
    engine.setProperty("rate", 190)
    speak(f"sir the current password is, {password}")


def snippingTool():
    """This funtion is for opening snipping toll"""
    try:
        speak("opening sir")
        pyautogui.hotkey("shift", 'win', 's')
    except:
        speak("sorry sir, for some reason i can't open this")


def esc():
    """This funtion is for escape"""
    pyautogui.hotkey("esc")


def deleteCache():
    """This funtion is for deleting jarvis cache"""
    try:
        speak("ok sir")
        shutil.rmtree('__pycache__')
        speak("successfully deleted")
    except:
        speak("sorry sir, i can't delete")


def translator():
    """This funtion is for opening translator"""
    try:
        speak("opening sir")
        webbrowser.open("www.google.com/search?q=translate+english+to+urdu&rlz=1C1GCEU_en&oq=translate&aqs=chrome.1.69i57j0i512j0i131i433i512j69i59j0i131i433i512l3j0i512l2j0i271.3247j0j7&sourceid=chrome&ie=UTF-8")
    except:
        speak("sorry sir, for some reason i can't open this")


def searchInYoutube():
    """This funtion is for searching in youtube"""
    try:
        speak("what should i search")
        content = takeCommand()
        move = pyautogui.locateOnScreen("images/youtube-search-img.PNG")
        editBut = pyautogui.center(move)
        pyautogui.moveTo(editBut)
        pyautogui.click()
        pyautogui.write(content, interval=0.03)
        pyautogui.hotkey("enter")
    except:
        speak("sorry sir, for some reason i can't search")


def reload():
    """This funtion is for reload the window"""
    speak("ok sir")
    pyautogui.hotkey("ctrl", "shift", "r")
