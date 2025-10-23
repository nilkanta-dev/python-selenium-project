
import base64
import time
import json
import re



class CDPTools:
	def __init__(self,driver):
		self.driver = driver
		self.mock_rules = {}

	#..............BASIC SETUP...............#

	def enable_network(self):
		self.driver.execute_cdp_cmd("Network.enable",{})

	def go_offline(self):
		self.driver.execute_cdp_cmd("Network.enable",{})
		self.driver.execute_cdp_cmd("Network.emulateNetworkConditions",{
			"offline":True,
			"latency":0,
			"downloadThroughput":0,
			"uploadThroughput":0
			})
		print("[CDP] Browser is now offline")

	def go_online(self):
		self.driver.execute_cdp_cmd("Network.emulateNetworkConditions",{
			"offline":False,
			"latency":0,
			"downloadThroughput":-1,
			"uploadThroughput":-1
			})
		print(f"[CDP] Browser is now online")

	def clear_browser_data(self):
		self.driver.execute_cdp_cmd("Network.clearBrowserCookies",{})
		self.driver.execute_cdp_cmd("Network.clearBrowserCache",{})
		print(f"[CDP] Cleared all cookies and caches")


	#..................GEO-LOCATION AND SCREENSHOT......................#

	def set_location(self,lat,lon,accuracy=100):
		self.driver.execute_cdp_cmd("Emulation.setGeolocationOverride",{
			"latitude":lat,
			"longitude":lon,
			"accuracy":accuracy
			})
		print(f"[CDP] Geolocation set to lat={lat} and lon={lon}")

	def take_full_screenshot(self,filename="screenshot.png"):
		result = self.driver.execute_cdp_cmd("Page.captureScreenshot",{"format":"png","fromSurface":True})
		with open(filename,"wb") as f:
			f.write(base64.b64decode(result["data"]))
		print(f"[CDP] Screenshot save as {filename}")


	#...................PERFORMANCE.....................#

	 
	#.................ADVANCED NETWORK....................#

	def block_urls(self,urls):
		self.driver.execute_cdp_cmd("Network.setBlockedURLs",{"urls":urls})
		print(f"[CDP] Blocked URLs:{urls}")

	

	#------------MOCKING VIA SELENIUM WIRE-----------------#

	def add_mock(self,url_pattern,mock_data):
		self.mock_rules[url_pattern] = mock_data

		def interceptor(request):
			for p, mock in self.mock_rules.items():
				if re.search (p,request.url):
					print(f"[Mocked] Intercepted {request.url}")
					request.create_response(
						status_code=200,
						headers={'Content-Type':'application/json'},
						body=json.dumps(mock)
						)
					return

		self.driver.request_interceptor = interceptor
		print(f"[CDP] Mock added for pattern: {url_pattern}")



	
	




