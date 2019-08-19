# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 23:42:52 2019

@author: kevin
"""
# le div montre que
# [<div id="main">
# <script src="/process/LastUpdate.js" type="text/javascript"></script>
# <script src="/process/tani_henkou.js" type="text/javascript"></script>
# <!--/#main --></div>]
# demandons à stack pcq je sais pas ce qui se passe
# https://pythonprogramminglanguage.com/web-scraping-with-pandas-and-beautifulsoup/

# le plus prometteur de 11h30  à 12h01
#https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f

# import libraries
import urllib.request
from bs4 import BeautifulSoup
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

df_list = pd.read_html(results[0].get_attribute('outerHTML'))
df = df_list[-1]
print(df)
df.to_csv('my_data.csv')

# create empty array to store data
data = []
# loop over results
# for result in results:
#     product_name = result.text
#     link = result.find_element_by_tag_name('a')
#     product_link = link.get_attribute("href")
#     # append dict to array
#     data.append({"product" : product_name, "link" : product_link})

# close driver 
driver.quit()



















# my_url = "https://kabu.com/investment/meigara/tani_henkou.html"
# from selenium import webdriver
# driver = webdriver.PhantomJS()
# driver.get(my_url)
# p_element = driver.find_elements_by_xpath("//*[@id='main']/table")
# print(p_element)

# # create empty array to store data
# data = []
# # loop over results
# for result in results:
#     product_name = result.text
#     link = result.find_element_by_tag_name('a')
#     product_link = link.get_attribute("href")
#     # append dict to array
#     data.append({"product" : product_name, "link" : product_link})
    
#     # close driver 
# driver.quit()
# # save to pandas dataframe
# df = pd.DataFrame(data)
# print(df)























# import lxml.html as lh
# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
# from tabulate import tabulate


# res = requests.get("https://kabu.com/investment/meigara/tani_henkou.html")
# kek = res.content
# soup = BeautifulSoup(res.text,'lxml')
# table = soup.find_all("div", {"id": "main"})
# print(table)
# # df = pd.read_html(str(table))
# # print( tabulate(df[0], headers='keys', tablefmt='psql') )
