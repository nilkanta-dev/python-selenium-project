
import base64

class CDPTools:
	def __init__(self,driver):
		self.driver = driver

	def enable_network(self):
		self.driver.execute_cdp_cmd("Network.enable",{})

	def go_offline(self):
		self.driver.execute_cdp_cmd("Network.enable",{})
		self.driver.execute_cdp_cmd("Network.enableNetworkConditions",{
			"offline":True,
			"latency":0,
			"downloadThroughput":0,
			"uploadThroughput":0
			})

	def go_online(self):
		self.driver.execute_cdp_cmd("Network.enableNetworkConditions",{
			"offline":False,
			"latency":0,
			"downloadThroughput":-1,
			"uploadThroughput":-1
			})

	def set_location(self,lat,lon,accuracy=100):
		self.driver.execute_cdp_cmd("Emulation.setGeolocationOverride",{
			"latitude":lat,
			"longitude":lon,
			"accuracy":accuracy
			})

	def clear_browser_data(self):
		self.driver.execute_cdp_cmd("Network.clearBrowserCookies",{})
		self.driver.execute_cdp_cmd("Network.clearBrowserCache",{})

	def take_full_screenshot(self,filename="screenshot.png"):
		result = self.driver.execute_cdp_cmd("Page.captureScreenshot",{"format":"png","fromSurface":True})
		with open(filename,"wb") as f:
			f.write(base64.b64decode(result["data"]))
		print(f"[CDP] Screenshot save as {filename}")

	def get_performance_metrics(self):
		self.driver.execute_cdp_cmd("Performance.enable",{})
		metrics = self.driver.execute_cdp_cmd("Performance.getMetrics",{})

		for m in metrics["metrics"]:
			print(f"{m['name']}:{m['value']}")



