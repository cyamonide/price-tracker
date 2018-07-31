from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import PTAmazon

urlsAmazon = [
	"https://www.amazon.ca/JBL-Waterproof-Portable-Bluetooth-Speaker/dp/B01F24RHF4/",
	"https://www.amazon.ca/JBL-Waterproof-Portable-Bluetooth-Speaker/dp/B01F24RHT0/",
	"https://www.amazon.ca/JBL-Waterproof-Portable-Bluetooth-Speaker/dp/B01F24RIKS/",
	"https://www.amazon.ca/JBL-Waterproof-Portable-Bluetooth-Speaker/dp/B01F24RI6M/"
]

options = Options()
options.set_headless(headless=True)

driver = webdriver.Firefox(firefox_options=options)

for url in urlsAmazon:
	print(str(PTAmazon.getPrice(url, driver)) + " | " + driver.title)	

driver.close()