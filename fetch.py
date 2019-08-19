# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:55:53 2019

@author: Kevin Chan
"""

"""
In the following URL, there is a list of 'stocks whose trading unit has changed'(売買単位変更銘柄一覧).
Create a program that prints it to standard output in a format that is easy to program (e.g. CSV format, etc.)

https://kabu.com/investment/meigara/tani_henkou.html


+ implementation computer language
  Anything is OK.

+ Condition
  Can be run on the command line under Linux etc.

example:
% ./fetch
2018/10/01,1728,ミサワ中国,1000,100
...


"""

# TODO arrange output (no col and row index) 
# TODO csv name add date
# TODO add dates to sleep
# TODO clean code and separate in functions
# TODO specify ddependencies

#https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f
import urllib.request
from selenium import webdriver
import time
import pandas as pd
# specify the url
urlpage = 'https://kabu.com/investment/meigara/tani_henkou.html' 
print(urlpage)
# run firefox webdriver from executable path of your choice
driver = webdriver.Firefox()


# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
print("see you in 5s")
time.sleep(5)
print("5s passed")

# find elements by xpath
results = driver.find_elements_by_xpath("//*[@id='main']/table")
print('Number of results', len(results))

#https://stackoverflow.com/a/49996714/9876427
df_list = pd.read_html(results[0].get_attribute('outerHTML'))
df = df_list[-1]
print(df)
df.to_csv('trading_unit_changed_stocks.csv')

# close driver 
driver.quit()    

#if __name__ == "__main__":
        
