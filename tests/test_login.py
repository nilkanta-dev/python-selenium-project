import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login import LoginPage


def test_login_url(driver):
	driver.get("https://automationexercise.com/login")
	assert "Login to your account" in driver.page_source

def test_login(driver,credentials):
	driver.get("https://automationexercise.com/login")

	login_in = LoginPage(driver)
	login_in.login(**credentials)

	
	page_source = driver.page_source

	assert "Logged in as" in page_source

	logging.info("Logged in as is found in page source")

