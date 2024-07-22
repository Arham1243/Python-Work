from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import pandas as pd

file = "send_dm.xlsx"
df = pd.read_excel(file)


if "msg_sent" in df.columns:
    untouched_df = df[(df["msg_sent"] == "no") | (df["msg_sent"].isna())]
    handles = df["handle"]
else:
    handles = df["handle"]

username = "webcodehaven6"
password = "@Admin!23#"
message = "Are you still open and offering services? I couldn't find your website. Are you still open?"


# Function to create a new Chrome webdriver instance with a specified user-agent
def get_chrome_driver(user_agent):
    chrome_options = Options()

    chrome_options.add_argument(f"user-agent={user_agent}")
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    return driver


def WaitForTheWebsiteToLoad(driver):
    try:
        # Wait for the navigation element to be present
        one = WebDriverWait(driver, 17).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input",
                )
            )
        )
        # Wait for the SKU element to be present
        two = WebDriverWait(driver, 17).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input",
                )
            )
        )
        # If both elements are found, return True
        return True
    except:
        # If any element is not found, return False
        return False


user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"

driver = get_chrome_driver(user_agent)
accounts_details = []
dm_link = "https://www.instagram.com/direct/inbox/"
link = "https://www.instagram.com/"


def close_popup():
    try:
        popup_close_btn = driver.find_element(
            By.XPATH,
            "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]",
        )
        if popup_close_btn:
            popup_close_btn.click()
    except Exception as e:
        print(e)


def login():
    driver.get(url=link)
    if WaitForTheWebsiteToLoad(driver):
        sleep(2)
        try:
            sleep(5)
            username_input = driver.find_element(
                By.XPATH,
                "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input",
            )
            password_input = driver.find_element(
                By.XPATH,
                "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input",
            )

            username_input.send_keys(username)

            password_input.send_keys(password)

            sleep(5)
            submit_btn = driver.find_element(
                By.XPATH,
                "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button",
            )
            submit_btn.click()
            sleep(10)
            driver.get(url=dm_link)
            sleep(8)
            close_popup()
            sleep(5)
        except Exception as e:
            print(e)


def move_cursor_to_color(color=(255, 144, 28)):
    try:
        # Capture screenshot of the entire screen
        screenshot = pyautogui.screenshot()
        screenshot = screenshot.convert("RGB")

        width, height = screenshot.size
        for x in range(width):
            for y in range(height):
                if screenshot.getpixel((x, y)) == color:
                    # Move the mouse to the location of the found color
                    pyautogui.moveTo(x, y)
                    print(f"Moved cursor to the color at ({x}, {y})")
                    return
        print("Color not found on the screen.")
    except Exception as e:
        print(f"An error occurred: {e}")


def update_sheet(handle, msg_sent):
    # Update the 'msg_sent' column where the 'handle' column matches the specified handle
    df.loc[df["handle"] == handle, "msg_sent"] = "yes" if msg_sent else "no"

    # Save the updated DataFrame to an Excel file
    df.to_excel(file, index=False)


def send_dm(handle, i):
    driver.get(url=dm_link)
    sleep(5)
    try:
        close_popup()
        send_msg_btn = driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div",
        )
        send_msg_btn.click()
        sleep(4)
        pyautogui.write(handle)
        sleep(5)
        pyautogui.hotkey("ctrl", "f")
        sleep(1)
        pyautogui.write(handle)
        if i == 0:
            pyautogui.hotkey("enter")
        pyautogui.hotkey("enter")
        sleep(1)
        move_cursor_to_color()
        sleep(1)
        pyautogui.click()
        sleep(2)
        pyautogui.hotkey("tab")
        pyautogui.hotkey("tab")
        pyautogui.hotkey("tab")
        pyautogui.hotkey("tab")
        pyautogui.hotkey("enter")
        sleep(3)
        pyautogui.write(message)
        pyautogui.hotkey("enter")
        sleep(2)
        try:
            msg_sent = driver.find_element(
                By.XPATH,
                "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div/div[1]/div/div/div[2]/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/div/div[2]",
            )
            print("msg Sent")
            update_sheet(handle, True)
        except NoSuchElementException:
            print("msg Not Sent")
            update_sheet(handle, False)
    except Exception as e:
        print(e)


if len(handles) > 0:
    login()
    for i, handle in enumerate(handles):
        send_dm(handle, i)
else:
    print("Message Sent to All Accounts ✅")
