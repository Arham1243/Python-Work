from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Import the Keys class

# Initialize the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the desired website
driver.get("https://www.youtube.com/")
time.sleep(15)

# Find the input tag using By.XPATH
input_xpath = "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input"  
input_element = driver.find_element(By.XPATH, input_xpath)

# Enter the search term
search_term = "zara dheera dheera clho mera sathiya hum bhi peecha hain tumhara"  # Replace with your desired search term
input_element.send_keys(search_term)

# Simulate pressing the Enter key
input_element.send_keys(Keys.RETURN)

# Wait for the search results to load (you can adjust the time as needed)
time.sleep(5)

# Close the browser
driver.quit()
