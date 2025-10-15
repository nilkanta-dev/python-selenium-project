from selenium.webdriver.common.by import By
from pages.base import BasePage


class LoginPage(BasePage):
	LOGIN_PAGE_LINK = (By.LINK_TEXT,"Signup / Login")

	#IN THE LOGIN PAGE TO LOGIN IN
	LOGIN_EMAIL_ID = (By.CSS_SELECTOR,"input[data-qa='login-email']")
	LOGIN_PASSWORD = (By.CSS_SELECTOR,"input[data-qa='login-password']")
	LOGIN_BUTTON = (By.CSS_SELECTOR,"button[data-qa='login-button']")

	#IN THE LOGIN PAGE
	REGISTER_NAME_INPUT = (By.CSS_SELECTOR,"input[data-qa='signup-name']")
	REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR,"input[data-qa='signup-email']")
	SIGNUP_BUTTON = (By.CSS_SELECTOR,"button[data-qa='signup-button']")

	#DETAILED SIGNUP
	TITLE = (By.CSS_SELECTOR,"input[id='id_gender1']")
	PASSWORD = (By.CSS_SELECTOR,"input[data-qa='password']")
	DAY_SELECT=(By.CSS_SELECTOR,"select[data-qa='days']")
	MONTH_SELECT=(By.CSS_SELECTOR,"select[data-qa='months']")
	YEAR_SELECT=(By.CSS_SELECTOR,"select[data-qa='years']")
	FIRST_NAME= (By.CSS_SELECTOR,"input[data-qa='first_name']")
	LAST_NAME = (By.CSS_SELECTOR,"input[data-qa='last_name']")
	ADDRESS = (By.CSS_SELECTOR,"input[data-qa='address']")
	COUNTRY = (By.CSS_SELECTOR,"select[data-qa='country']")
	STATE = (By.CSS_SELECTOR,"input[data-qa='state']")
	CITY = (By.CSS_SELECTOR,"input[data-qa='city']")
	ZIPCODE = (By.CSS_SELECTOR,"input[data-qa='zipcode']")
	MOBILE_NUMBER = (By.CSS_SELECTOR,"input[data-qa='mobile_number']")
	CREATE_ACCOUNT = (By.CSS_SELECTOR,"button[data-qa='create-account']")




	def login_url(self):
		self.click_element(self.LOGIN_PAGE_LINK)

	
	def register(self,name="markdoe",email="markdoe@test.com",password="1234512345"):
		self.input_text(self.REGISTER_NAME_INPUT,name)
		self.input_text(self.REGISTER_EMAIL_INPUT,email)
		self.click_element(self.SIGNUP_BUTTON)

		self.click_element(self.TITLE)
		self.input_text(self.PASSWORD,password)
		self.select_dropdown(self.DAY_SELECT,"15")
		self.select_dropdown(self.MONTH_SELECT,"December",by="text")
		self.select_dropdown(self.YEAR_SELECT,"2018")

		self.input_text(self.FIRST_NAME,"mark")
		self.input_text(self.LAST_NAME,"doe")
		self.input_text(self.ADDRESS,"123Street")
		self.select_dropdown(self.COUNTRY,"India")
		self.input_text(self.STATE,"Gujrat")
		self.input_text(self.CITY,"Ahmedabad")
		self.input_text(self.ZIPCODE,"12345")
		self.input_text(self.MOBILE_NUMBER,"0123456789")
		self.click_element(self.CREATE_ACCOUNT)


	def login(self,email='markdoe@test.com',password=1234512345):
		self.input_text(self.LOGIN_EMAIL_ID,email)
		self.input_text(self.LOGIN_PASSWORD,password)
		self.click_element(self.LOGIN_BUTTON)
