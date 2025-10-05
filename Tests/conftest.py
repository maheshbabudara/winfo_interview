from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
import pytest
from Utilities.interview_locator import Login_locators

@pytest.fixture()
def winfo():
    username="casey.brown"
    password="m*5fP?2Y"
    option=Options()
    winfo=WebDriver(options=option)
    winfo.get("https://eudr-dev16.ds-fa.oraclepdemos.com/fscmUI/faces/AtkHomePageWelcome")
    winfo.implicitly_wait(10)
    winfo.maximize_window()

    username_loc=Login_locators[0]
    password_loc=Login_locators[1]
    signin_loc=Login_locators[2]

    winfo.find_element(*username_loc).send_keys(username)
    winfo.find_element(*password_loc).send_keys(password)
    winfo.find_element(*signin_loc).click()

    yield winfo
    winfo.close()
#check