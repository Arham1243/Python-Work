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
from jarvisFunctions import speak, takeCommand, takeCommandSearch, youtube, openFirefox, google, liveServer, mySheet, searchInGoogle, searchInPortable, yandex, firefoxPortable, fontAwesome, boxIcon, passwordChange, currentTimeFunc, todayDateFunc, snippingTool, vsCode, fullWindow, photoshop, output, xampp, colourPicker, outlook, typeIt, enter, enter, translator, searchInYoutube, switchWindow, reopenTheTab, reload, closeWindow, closeTab, shutdown, lock, restart, closeProgram, deleteCache, currentPassword


# All Tasks That Jarvis Can Do


def main():
    try:
        # print("Tell A Password")
        # speak("Tell A Password")
        # userSaid = takeCommand().lower()
        # if userSaid == password:
        #     print("Welcome Back Sir")
        #     speak("Welcome Back Sir")
        from jarvisFunctions import wishMe
        wishMe()
        while True:
            query = takeCommand().lower()
            if 'open youtube' in query:
                youtube()

            elif 'open firefox' in query:
                openFirefox()

            elif 'open google' in query:
                google()

            elif 'open live server' in query:
                liveServer()

            elif 'open my task sheet' in query:
                mySheet()

            elif 'search in google' in query:
                searchInGoogle()

            elif 'who are you' in query:
                speak(
                    "i am jarvis, i am an artificial intelligence, arham made me, with the help of python language")

            elif 'what you can do' in query:
                speak("i can do whatever you want")

            elif 'nice to meet you' in query:
                speak("nice to meet you too")

            elif 'google search' in query:
                engine.setProperty("rate", 190)
                import wikipedia as wkp
                query = query.replace("google search", "")
                speak("this is what i found")
                pywhatkit.search(query)

                try:
                    results = wkp.summary(query, 2)
                    print(results)
                    speak(results)
                except:
                    speak("sorry sir i cant found")

            elif 'search in portable' in query:
                searchInPortable()

            elif 'open yandex' in query:
                yandex()

            elif 'this is not a command' in query:
                speak("sorry sir")

            elif 'firefox portable' in query:
                firefoxPortable()

            elif 'open font awesome' in query:
                fontAwesome()

            elif 'open box icon' in query:
                boxIcon()

            elif 'change the password of' in query:
                passwordChange()

            elif 'time' in query:
                currentTimeFunc()

            elif 'date' in query:
                todayDateFunc()

            elif 'delete cache' in query:
                deleteCache()

            elif 'clear cache' in query:
                deleteCache()

            elif 'open snipping tool' in query:
                snippingTool()

            elif 'open vs code' in query:
                vsCode()

            elif 'full window' in query:
                fullWindow()

            elif 'open photoshop' in query:
                photoshop()

            elif 'open output' in query:
                output()

            elif 'open xampp' in query:
                xampp()

            elif 'colour picker' in query:
                colourPicker()

            elif 'open outlook' in query:
                outlook()

            elif 'type it' in query:
                typeIt()

            elif 'hit enter' in query:
                enter()

            elif 'send message' in query:
                enter()

            elif 'open translator' in query:
                translator()

            elif 'search in youtube' in query:
                searchInYoutube()

            elif 'the current password' in query:
                currentPassword()

            elif 'switch the tab' in query:
                switchWindow()

            elif 'reopen the tab' in query:
                reopenTheTab()

            elif 'hello jarvis' in query:
                speak("yes Arham")

            elif 'reload the window' in query:
                reload()

            elif 'close the window' in query:
                closeWindow()

            elif 'close the tab' in query:
                closeTab()

            elif 'are you here' in query:
                speak("yes sir, i am here")

            elif 'shutdown the computer' in query:
                shutdown()

            elif 'lock the computer' in query:
                lock()

            elif 'restart the computer' in query:
                restart()

            elif 'message to' in query:
                try:
                    move = pyautogui.locateOnScreen(
                        "images/output-search-img.PNG")
                    editBut = pyautogui.center(move)
                    pyautogui.moveTo(editBut)
                    pyautogui.click()
                    query = query.replace("message to", "")
                    pyautogui.write(query, interval=0.03)
                    pyautogui.hotkey("enter")
                    speak("what should i message")
                    content = takeCommandSearch()
                    pyautogui.write(content, interval=0.03)
                    pyautogui.hotkey("enter")
                except:
                    engine.setProperty("rate", 200)
                    print(
                        "you are not in output messenger if you want to open output just say open output")
                    speak(
                        "you are not in output messenger if you want to open output just say open output")

            elif 'ok jarvis close it' in query:
                closeProgram()
        # else:
        #     engine.setProperty("rate", 190)
        #     print("You Can't Open It without Arham's Permission")
        #     speak("You Can't Open It without Arham's Permission")
    except:
        print("Sir Please Plug Your Microphone In System Before Giving Any Command")
        speak("Sir Please Plug Your Microphone In System Before Giving Any Command")
