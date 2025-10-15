from selenium.webdriver.common.by import By

from pages.base import BasePage


class LandingPage(BasePage):

	ADD_TO_CART = (By.CSS_SELECTOR,"[data-product-id='1']")
	PRODUCT_DETAIL = (By.LINK_TEXT,"View Product")
	DISMISS_MODAL = (By.CSS_SELECTOR,"button[data-dismiss='modal']")


	def open_homepage(self):
		self.driver.get("https://automationexercise.com")

	def add_to_cart(self):
		
		self.click_element(self.ADD_TO_CART)
		self.click_element(self.DISMISS_MODAL)

	def open_product_detail(self):
		self.click_element(self.PRODUCT_DETAIL)
		self.driver.back()