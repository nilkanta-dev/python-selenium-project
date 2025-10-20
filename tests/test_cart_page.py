from pages.cart_page import CartPage
from pages.landing_page import LandingPage
import allure
import time


@allure.title("Test item removal from cart")
@allure.description("This test tests item removal from cart after logging in and adding item to the cart.")
def test_go_to_cart(logged_in_user):

	driver = logged_in_user

	with allure.step("Add to cart"):
		LandingPage(driver).add_to_cart()

	with allure.step("Go to cart"):
		CartPage(driver).go_to_cart()
		assert "Shopping Cart" in driver.page_source

	with allure.step("Remove item from cart"):
		CartPage(driver).remove_item()
		time.sleep(5)
		assert "Cart is empty!" in driver.page_source


