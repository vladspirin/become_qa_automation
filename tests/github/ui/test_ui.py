from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_github_login_negative():
    # create webdriver object
    driver = webdriver.Safari()

    # open the browser
    # navigate to login page
    driver.get("https://github.com/login")

    # enter wrong creds
    login_github = driver.find_element(By.ID, "login_field")
    login_github.send_keys("login#gmail.com")

    password_github = driver.find_element(By.ID, "password")
    password_github.send_keys("password")

    # click button
    login_button_github = driver.find_element(By.NAME, "commit")
    login_button_github.click()

    # check error message
    flash_error_msg = driver.find_element(By.CLASS_NAME, "flash-error")
    time.sleep(5)
    assert error_msg is not None
