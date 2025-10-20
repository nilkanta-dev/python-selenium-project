from selenium.webdriver.common.by import By
from pages.base import BasePage


class CartPage(BasePage):

	GO_TO_CART = (By.LINK_TEXT,'Cart')
	REMOVE_ITEM = (By.CSS_SELECTOR,'a.cart_quantity_delete')


	def go_to_cart(self):
		self.click_element(self.GO_TO_CART)

	def remove_item(self):
		self.click_element(self.REMOVE_ITEM)
