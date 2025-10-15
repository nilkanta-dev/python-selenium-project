from shopping import Shopping


with Shopping(teardown=False) as bot:
	bot.landing_page()
	bot.login_page()