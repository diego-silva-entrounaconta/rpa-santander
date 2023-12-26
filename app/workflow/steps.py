from selenium.webdriver.chrome.webdriver import WebDriver
from ui import login, navigate


def step_one(driver: WebDriver):
    login.make_login(driver)


def step_two(driver: WebDriver):
    navigate.navigate_to_consigned(driver)


def step_three(driver: WebDriver):
    navigate.navigate_to_proposal(driver)
