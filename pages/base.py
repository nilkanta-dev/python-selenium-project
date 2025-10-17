from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select




class BasePage:
	def __init__(self,driver):
		self.driver = driver
		self.wait = WebDriverWait(driver,20)


	def click_element(self,locator,retries=2):
		for attempt in range(retries):
			try:
		    	element = self.wait.until(EC.element_to_be_clickable(locator))
		    	self.driver.execute_script("arguments[0].scrollIntoView(true);",element)
		    	ActionChains(self.driver).move_to_element(element).perform()
		    	element.click()

			except Exception as e:
				self.driver.save_screenshot("click_intercepted_error.png")
				print(f"Attempt {attempt + 1} failed:{e}")
				if attempt == retries - 1:
				raise
		

	def input_text(self,locator,text):
		element = self.wait.until(EC.visibility_of_element_located(locator))
		element.clear()
		element.send_keys(text)

	def select_dropdown(self,locator,value,by='value'):
		element = self.wait.until(EC.visibility_of_element_located(locator))
		self.driver.execute_script("arguments[0].scrollIntoView(true);",element)
		try:
			ActionChains(self.driver).move_to_element(element).perform()
		except Exception:
			pass

		select = Select(element)

		if by == 'text':
			select.select_by_visible_text(value)
		elif by == 'index':
			select.select_by_index(int(value))
		else:
			select.select_by_value(value)
