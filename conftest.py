import pytest
from selenium import webdriver
import logging
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import requests

load_dotenv()

logging.basicConfig(level=logging.INFO)

#-----FOR LOCAL TESTING------#
# @pytest.fixture()

# def driver():
	
# 	driver = webdriver.Firefox()
# 	driver.maximize_window()
# 	yield driver
# 	driver.quit()


#---------FOR LOCAL PARALLEL TESTING---------------#

# @pytest.fixture(params=["chrome","firefox"])

# def driver(request):
# 	browser = request.param
# 	if browser == 'chrome':
# 		driver = webdriver.Chrome()
# 	elif browser == 'firefox':
# 		driver = webdriver.Firefox()
# 	else:
# 		raise ValueError("Unsupported Error")


# 	driver.maximize_window()
# 	yield driver
# 	driver.quit()

#---------FOR TESTING WITH SELENIUM GRID------------#
# @pytest.fixture(params=["chrome","firefox"])
# def driver(request):
# 	grid_url = "http://localhost:4444/wd/hub"

# 	if request.param == "chrome":
# 		options = webdriver.ChromeOptions()
# 	elif request.param == "firefox":
# 		options = webdriver.FirefoxOptions()

# 	driver = webdriver.Remote(command_executor=grid_url,options=options)
# 	yield driver
# 	driver.quit()

#------------FOR TESTING WITH JENKINS-----------#

@pytest.fixture(params=["chrome"])
def driver(request):
    grid_url = "http://selenium-standalone-chrome:4444/wd/hub"


    # Wait for Selenium to be ready
    for _ in range(30):
        try:
            r = requests.get(f"{grid_url}/status")
            if r.status_code == 200:
                break
        except requests.exceptions.RequestException:
            pass
        time.sleep(1)
    else:
        raise RuntimeError("Selenium Grid not ready")

	


    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Remote(command_executor=grid_url, options=options)
    elif request.param == "firefox":
    	options = FirefoxOptions()
    	options.add_argument("--headless")
    	driver = webdriver.Remote(command_executor=grid_url,options=options)

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()

def credentials():
	email = os.getenv('TEST_USER_EMAIL')
	password = os.getenv('TEST_USER_PASSWORD')
	if not email or not password:
		raise RuntimeError("Missing TEST_USER_EMAIL or TEST_USER_PASSWORD in environment variables")
	return {"email":email,"password":password}
