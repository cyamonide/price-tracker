from selenium import webdriver

def get_text_excluding_children(driver, element):
	return driver.execute_script("""
	return jQuery(arguments[0]).contents().filter(function() {
			return this.nodeType == Node.TEXT_NODE;
	}).text();
	""", element)