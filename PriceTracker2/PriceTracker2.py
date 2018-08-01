from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import datetime
import numpy as np

import PTAmazon
import PTTheSource
import PTBestBuy
import PTStaples
import PTNewegg

now = datetime.datetime.now()

urlsAmazon = [
	"https://www.amazon.ca/JBL-Waterproof-Portable-Bluetooth-Speaker/dp/B01F24RHF4/",
	"https://www.amazon.ca/JBL-Waterproof-Portable-Bluetooth-Speaker/dp/B01F24RHT0/",
	"https://www.amazon.ca/JBL-Waterproof-Portable-Bluetooth-Speaker/dp/B01F24RIKS/",
	"https://www.amazon.ca/JBL-Waterproof-Portable-Bluetooth-Speaker/dp/B01F24RI6M/",
	"https://www.amazon.ca/Transcend-256GB-MTS400-Solid-TS256GMTS400S/dp/B075P1JSGL/"
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

urlsNewegg = [
	"https://www.newegg.ca/Product/Product.aspx?Item=N82E16820168038"
]

pricesProd1 = []
pricesProd2 = []
pricesProd3 = []

options = Options()
options.set_headless(headless=True)

print("Initializing webdriver...")

driver = webdriver.Firefox(firefox_options=options)

print("\t\t***** Amazon ***** ")
for url in urlsAmazon:
	retval = PTAmazon.getPrice(url, driver)
	print(str(retval) + " | " + driver.title)
	pricesProd1.append(retval)

print("\t\t***** The Source ***** ")
for url in urlsTheSource:
	retval = PTTheSource.getPrice(url, driver)
	print(str(retval) + ".xx | " + driver.title)
	pricesProd1.append(retval)

print("\t\t***** Best Buy ***** ")
for url in urlsBestBuy:
	retval = PTBestBuy.getPrice(url, driver)
	print(str(retval) + " | " + driver.title)
	pricesProd1.append(retval)

print("\t\t***** Staples ***** ")
for url in urlsStaples:
	retval = PTStaples.getPrice(url, driver)
	print(str(retval) + " | " + driver.title)
	pricesProd1.append(retval)

print("\t\t***** Newegg ***** ")
for url in urlsNewegg:
	retval = PTNewegg.getPrice(url, driver)
	print(str(retval) + " | " + driver.title)
	pricesProd1.append(retval)

np.savetxt('prod1.db', pricesProd1, delimiter=' ')

driver.close()