from shopping import Shopping
from pages.cdp_utils import CDPTools
import time


with Shopping(teardown=False) as bot:
	bot.landing_page()
	bot.cdp = CDPTools(bot.driver)

	bot.cdp.clear_browser_data()
	bot.cdp.block_urls(["https://fundingchoicesmessages.google.com"])
	bot.cdp.add_mock(r"add_to_cart/\d+", {
    "status": "success",
    "message": "Mocked product added to cart"
})

	input("Press Enter when you are done inspecting the browser…")  # pause here to keep the window open
	
	
	# Example offline simulation
	# bot.cdp.go_offline()
	# time.sleep(2)
	# bot.cdp.go_online()
	# bot.driver.refresh()


	
	# bot.cart_page()
	# bot.login_page()
	# bot.use_cdp_tools()