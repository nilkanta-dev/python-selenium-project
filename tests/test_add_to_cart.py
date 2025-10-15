from pages.landing_page import LandingPage

def test_add_to_cart(driver):
	driver.get('https://automationexercise.com')

	products_page = LandingPage(driver)

	products_page.add_to_cart()

	page_source = driver.page_source

	assert "Added" in page_source,"'Added' text not found in page source"

	print("'Added' text found in page source")

