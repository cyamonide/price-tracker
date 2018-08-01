from selenium import webdriver

from PTHelper import get_text_excluding_children

def getPrice(url, driver):
	
	driver.get(url)

	elem = driver.find_element_by_xpath("//meta[@itemprop='price']")
	rawPrice = elem.get_attribute("content")

	assert "No results found." not in driver.page_source

	return float(rawPrice.split()[-1])