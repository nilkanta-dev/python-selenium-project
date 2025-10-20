import logging
from pages.login_page import LoginPage
import pytest
import allure



def test_login_url(driver):
	driver.get('https://automationexercise.com/')
	login_page_url = LoginPage(driver)
	login_page_url.login_url()
	assert "Login to your account" in driver.page_source




#------------Using Hardcoded User Details-------------#

# @pytest.mark.parametrize("credentials",[

# 	{"email":"user1@test.com","password":"12345"},
# 	{"email":"user2@test.com","password":"123456"},
# 	{"email":"user3@test.com","password":"123457"}
# ])


# def test_login(driver,credentials):
# 	driver.get("https://automationexercise.com/login")

# 	login_page = LoginPage(driver)
# 	login_page.login(**credentials)

	
# 	page_source = driver.page_source

# 	assert "Logged in as" in page_source

# 	logging.info("Logged in as is found in page source")


#---------------Using External File(CSV) for user data--------------#

@pytest.mark.regression

def test_login(driver,credentials):

	driver.get("https://automationexercise.com/login")

	login_page = LoginPage(driver)
	login_page.login(**credentials)
	assert "Logged in as" in driver.page_source

