from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import PTAmazon
import PTTheSource
import PTBestBuy
import PTStaples

urlsAmazon = [
	"https://www.amazon.ca/JBL-Waterproof-Portable-Bluetooth-Speaker/dp/B01F24RHF4/",
	"https://www.amazon.ca/JBL-Waterproof-Portable-Bluetooth-Speaker/dp/B01F24RHT0/",
	"https://www.amazon.ca/JBL-Waterproof-Portable-Bluetooth-Speaker/dp/B01F24RIKS/",
	"https://www.amazon.ca/JBL-Waterproof-Portable-Bluetooth-Speaker/dp/B01F24RI6M/"
]

urlsTheSource = [
	"https://www.thesource.ca/en-ca/p/108059964"
]

urlsBestBuy = [
	"https://www.bestbuy.ca/en-ca/product/jbl-jbl-charge-3-waterproof-wireless-bluetooth-speaker-black-jblcharge3blkam/10424278.aspx?"
]

urlsStaples = [
	"https://www.staples.ca/en/JBL-Charge-3-Portable-Bluetooth-Waterproof-Speaker-Black/product_2300581_1-CA_1_20001"
]

options = Options()
options.set_headless(headless=True)

print("Initializing webdriver...")

driver = webdriver.Firefox(firefox_options=options)

print("\t\t***** Amazon ***** ")
for url in urlsAmazon:
	print(str(PTAmazon.getPrice(url, driver)) + " | " + driver.title)

print("\t\t***** The Source ***** ")
for url in urlsTheSource:
	print(str(PTTheSource.getPrice(url, driver)) + ".xx | " + driver.title)

print("\t\t***** Best Buy ***** ")
for url in urlsBestBuy:
	print(str(PTBestBuy.getPrice(url, driver)) + " | " + driver.title)

print("\t\t***** Staples ***** ")
for url in urlsStaples:
	print(str(PTStaples.getPrice(url, driver)) + " | " + driver.title)

driver.close()