# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:55:53 2019

@author: Kevin Chan
"""

import datetime
import time

import urllib.request
from selenium import webdriver
import pandas as pd

# Reference :
# https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f

# Specify the url
url = 'https://kabu.com/investment/meigara/tani_henkou.html' 
print("Accessing ", url, "\n")

# Run firefox webdriver
driver = webdriver.Firefox()
driver.get(url)
# Scroll down the page to load the whole page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

print("Started sleeping for 5 seconds at ", datetime.datetime.now())
time.sleep(5)
print("Sleep finished", "\n")

print("Parsing webpage ... \n")
# Find elements by xpath
results = driver.find_elements_by_xpath("//*[@id='main']/table")
# Parse the stocks table
df_list = pd.read_html(results[0].get_attribute('outerHTML'))

# Close driver 
driver.quit()

print("Parsing done \n")

# Save to csv file, and print to console
df = df_list[-1]
df.to_csv('trading_unit_changed_stocks.csv', header=False, index=False, encoding='utf_8_sig')
print(df)
