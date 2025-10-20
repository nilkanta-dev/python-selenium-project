from selenium import webdriver
from pages.landing_page import LandingPage
from pages.login import LoginPage
from pages.cart import CartPage
from pages.cdp_utils import CDPTools

class Shopping:
	def __init__(self,teardown=True):
		self.driver = webdriver.Firefox()
		# self.driver = webdriver.Chrome()
		self.teardown = teardown
		self.driver.maximize_window()

	def __enter__(self):
		return self

	def __exit__(self,exc_type,exc_value,traceback):
		if self.teardown:
			self.driver.quit()


	def landing_page(self):
		self.landing = LandingPage(self.driver)
		self.landing.open_homepage()
		self.landing.add_to_cart()
		self.landing.open_product_detail()

	def login_page(self):
		self.login = LoginPage(self.driver)
		self.login.login_url()
		self.login.register()
		self.login.login()

	def cart_page(self):
		self.cart = CartPage(self.driver)
		self.cart.go_to_cart()
		self.cart.remove_item()

	def use_cdp_tools(self):
		self.cdp = CDPTools(self.driver)
		self.cdp.enable_network()
		self.cdp.take_full_screenshot()
		self.cdp.get_performance_metrics()

