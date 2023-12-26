import dotenv
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from workflow import steps
from configuration import settings
from time import sleep

# Load environment variables from .env file
dotenv.load_dotenv()

# Access environment variables
url = os.getenv("URL")


def main():
    print("Starting...")

    # Add arguments to browser options
    opt = Options()
    for index, args in enumerate(settings.arguments):
        opt.add_argument(args)

    # Create the browser instance and open
    chrome_path = os.environ.get("CHROMEDRIVER_PATH")
    service = Service(chrome_path)

    driver = webdriver.Chrome(service=service, options=opt)
    driver.get(url)

    sleep(5)

    driver.implicitly_wait(5)

    print("Step one")
    # Calling step by step
    steps.step_one(driver)

    print("Step two")
    sleep(1)
    steps.step_two(driver)

    print("Step three")
    sleep(3)
    steps.step_three(driver)

    input("Press to quit")
    driver.quit()


if __name__ == "__main__":
    main()