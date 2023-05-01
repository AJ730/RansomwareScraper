from threading import Event

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import logger.log
from logger import log


class ChromeSimulator():

	def __init__(self, d="/chrome_simulator/chromedriver"):
		"""
		Initialize chrome Driver
		@param d: full path of chrome driver
		@type d: string
		"""
		edge_options = Options()
		edge_options.add_argument("ignore-certificate-error")
		edge_options.add_argument("ignore-ssl-errors")


		self.driver = webdriver.Edge(d)
		self.w = WebDriverWait(self.driver, 10)
		log.info("Succesfully started Chromium Based Browser")

	def get_driver(self):
		"""
		Return current driver
		@return: driver
		@rtype: driver
		"""
		return self.driver

	def get_browser(self):
		"""
		Get google
		@return: google search
		@rtype: void
		"""
		self.driver.maximize_window()
		self.driver.get("https://www.google.com/")

	def accept_cookies(self):
		buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Allow')]")  # Try Finding Cookies
		buttons.extend(
			self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Accepteren')]"))  # Try Finding Cookies
		buttons.extend(
			self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Accept')]"))  # Try Finding Cookies
		for button in buttons:
			button.click()

	def accept_license(self):
		"""
		Accept google license
		@return: void
		@rtype: void
		"""
		agree = self.driver.find_element(By.ID, "L2AGLb")
		agree.click()
		log.warning("Accepted License")

	def search_by_name(self, query):
		"""
		Search google
		@param query: query
		@type query: string
		@return: searched step
		@rtype: void
		"""
		element = self.driver.find_element(By.NAME, query)
		element.send_keys(query)
		element.submit()



	def search_by_id(self, id):
		"""
		Search google
		@param query: query
		@type query: string
		@return: searched step
		@rtype: void
		"""
		element = self.driver.find_element(By.ID, id)
		element.send_keys(id)
		element.submit()

	def search_by_Xpath(self, xpath, payload):
		"""
		Submit payload using XPATH
		@param xpath: XPATH
		@type payload: payload
		@return: submit payload
		@rtype: none
		"""
		element = self.driver.find_element(By.XPATH, xpath)
		element.send_keys(payload)
		element.submit()

	def search_by_query(self, query):
		"""
		Submit payload as a query
		@param query: query
		@type query: query
		@return: go to the query
		@rtype: none
		"""
		self.driver.get(query)

	def get_current_address_url(self):
		"""
		Get current webpage url
		@return: url
		@rtype: string
		"""
		return self.driver.current_url

	def halt(self, seconds):
		"""
		Stop current thread in seconds
		@param seconds: time
		@type seconds: int
		@return: halt execution
		@rtype: void
		"""
		Event().wait(seconds)

	def kill_chrome(self):
		"""
		Close Chrome Browser
		@return: stopped Chrome
		@rtype: stopped Chrome
		"""
		self.driver.quit()
