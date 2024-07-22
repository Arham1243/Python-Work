from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to create a new Chrome webdriver instance with a specified user-agent
def get_chrome_driver(user_agent):
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={user_agent}")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    return driver


accounts = [
    {
        "name": "BenjaminMoore",
        "email": "kusrwdp9@hotmail.com",
        "password": "JiMhb5Pc",
    },
    {
        "name": "AvaSmith",
        "email": "3rafjq5v@gmail.com",
        "password": "1hxPDxAC",
    },
    {
        "name": "MichaelJones",
        "email": "noig1wqf@gmail.com",
        "password": "0PR0FRuN",
    },
    {
        "name": "IsabellaTaylor",
        "email": "n8uprzza@yahoo.com",
        "password": "6rCfibVW",
    },
    {
        "name": "OliviaJones",
        "email": "ngovzqa0@hotmail.com",
        "password": "Y5qwBeXg",
    },
    {
        "name": "AvaTaylor",
        "email": "fj1oyiep@example.com",
        "password": "bkSHzfbk",
    },
    {
        "name": "OliviaMoore",
        "email": "fbzdv2nx@example.com",
        "password": "Yzv0KpIo",
    },
    {
        "name": "SophiaDavis",
        "email": "8gs7h84x@outlook.com",
        "password": "QCBVMpNG",
    },
]


def WaitForTheWebsiteToLoad(driver):
    try:
        # Wait for the navigation element to be present
        one = WebDriverWait(driver, 17).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/form/div[3]/div/table/tbody/tr[3]/td[2]/div/table/tbody/tr[2]/td[3]/input",
                )
            )
        )
        # Wait for the SKU element to be present
        two = WebDriverWait(driver, 17).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/form/div[3]/div/table/tbody/tr[3]/td[2]/div/table/tbody/tr[3]/td[3]/input",
                )
            )
        )
        # If both elements are found, return True
        return True
    except:
        # If any element is not found, return False
        return False

def process_accounts(account):
    user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
    # Create a new Chrome webdriver instance with the specified user-agent
    driver = get_chrome_driver(user_agent)
    accounts_details = []
    link = "https://www.ocrwebservice.com/account/signup"
    driver.get(url=link)
    if WaitForTheWebsiteToLoad(driver):
        sleep(2)
        try:
            sleep(5)
            username_input = driver.find_element(
                By.XPATH,
                "/html/body/form/div[3]/div/table/tbody/tr[3]/td[2]/div/table/tbody/tr[2]/td[3]/input",
            )
            email_input = driver.find_element(
                By.XPATH,
                "/html/body/form/div[3]/div/table/tbody/tr[3]/td[2]/div/table/tbody/tr[3]/td[3]/input",
            )
            password_input = driver.find_element(
                By.XPATH,
                "/html/body/form/div[3]/div/table/tbody/tr[3]/td[2]/div/table/tbody/tr[4]/td[3]/input",
            )
            con_password_input = driver.find_element(
                By.XPATH,
                "/html/body/form/div[3]/div/table/tbody/tr[3]/td[2]/div/table/tbody/tr[5]/td[3]/input",
            )
            privacy_policy_checkbox = driver.find_element(
                By.XPATH,
                "/html/body/form/div[3]/div/table/tbody/tr[3]/td[2]/div/table/tbody/tr[8]/td[2]/span[1]/input",
            )

            username_input.send_keys(account["name"])
            email_input.send_keys(account["email"])
            password_input.send_keys(account["password"])
            con_password_input.send_keys(account["password"])
            # Check if the checkbox is already selected
            if not privacy_policy_checkbox.is_selected():
                # If not selected, click to select it
                privacy_policy_checkbox.click()
                print("Privacy policy checkbox selected.")
            else:
                print("Privacy policy checkbox is already selected.")
            sleep(5)
            submit_btn = driver.find_element(
                By.XPATH,
                "/html/body/form/div[3]/div/table/tbody/tr[3]/td[2]/div/table/tbody/tr[9]/td[3]/input",
            )
            submit_btn.click()
            sleep(7)

            new_username_tag = driver.find_element(
                By.XPATH,
                "/html/body/form/div[3]/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/span",
            )
            new_key_tag = driver.find_element(
                By.XPATH,
                "/html/body/form/div[3]/div/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td[2]/span",
            )
            new_username = new_username_tag.text
            new_key = new_key_tag.text
            accounts_info = {
                "username": new_username,
                "License API": new_key,
            }
            print(accounts_info)
            accounts_details.append(accounts_info)
        except Exception as e:
            print(e)
    else:
        print("Website did not load within the timeout period.")

    # Close the webdriver session
    driver.quit()
    return accounts_details

# Process accounts
all_accounts_details = []
for account in accounts:
    all_accounts_details.extend(process_accounts(account))

# Print the combined results
print(all_accounts_details)