import dotenv
import os

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Load environment variables from .env file
dotenv.load_dotenv()

# Access environment variables
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")


def make_login(driver: WebDriver):

    # Search for inputs
    input_login = driver.find_element(by=By.ID, value="userLogin__input")
    input_password = driver.find_element(by=By.ID, value="userPassword__input")

    # Wait for the inputs to be on screen and fill them in
    driver.implicitly_wait(2)
    input_login.send_keys(login)
    input_password.send_keys(password)

    # Press Enter
    action = ActionChains(driver)
    action.key_down(Keys.ENTER).perform()
