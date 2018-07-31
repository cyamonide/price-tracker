from selenium import webdriver

from PTHelper import get_text_excluding_children

def getPrice(url, driver):
	
	driver.get(url)

	assert "JBL" in driver.title
	elem = driver.find_element_by_xpath("//span[@ng-show='priceWarrantyData.pricing.priceOfLowestPriceSKU.lowestPrice <= 0']")
	rawPrice = get_text_excluding_children(driver, elem)

	assert "No results found." not in driver.page_source

	return float(rawPrice.split()[-1][1:])