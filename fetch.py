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

import requests
import lxml.html as lh
import pandas as pd
import urllib
from bs4 import BeautifulSoup
from tabulate import tabulate

def fetch_html_table():
    print(heh)


"""
reference used : https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059
"""
if __name__ == '__main__':
    # url = 'https://kabu.com/investment/meigara/tani_henkou.html'
    # html = requests.get(url).content
    # df_list = pd.read_html(html)
    # df = df_list[-1]
    # print(df)
    # df.to_csv('my data.csv')
    
    
    
    #pd.read_html(requests.get(https://kabu.com/investment/meigara/tani_henkou.html).content)[-1].to_csv("fetch.csv")
    
    # https://pythonprogramminglanguage.com/web-scraping-with-pandas-and-beautifulsoup/
    res = requests.get("https://kabu.com/investment/meigara/tani_henkou.html")
    soup = BeautifulSoup(res.content,'lxml')
    table = soup.find_all("table")
    print(table)
    # df = pd.read_html(str(table))
    # print( tabulate(df[0], headers='keys', tablefmt='psql') )
    
    
    # reference : https://stackoverflow.com/questions/10556048/how-to-extract-tables-from-websites-in-python/44506462
    # web = urllib.urlopen("https://kabu.com/investment/meigara/tani_henkou.html")
    # s = web.read()
    
    # html = etree.HTML(s)
    
    # ## Get all 'tr'
    # tr_nodes = html.xpath('//table[class="tbl01"]/tr')
    
    # ## 'th' is inside first 'tr'
    # header = [i[0].text for i in tr_nodes[0].xpath("th")]
    
    # ## Get text from rest all 'tr'
    # td_content = [[td.text for td in tr.xpath('td')] for tr in tr_nodes[1:]]
    
    
    # url = 'https://kabu.com/investment/meigara/tani_henkou.html'

    # #Create a handle, page, to handle the contents of the website
    # page = requests.get(url)
    # #Store the contents of the website under doc
    # doc = lh.fromstring(page.content)
    # print(doc)
    # #Parse data that are stored between <tr>..</tr> of HTML
    # tr_elements = doc.xpath('//tr')
    
    # #Check the length of the first 12 rows
    # print(len(tr_elements))
    # for T in tr_elements[:12]:
    #     print(len(T))
        
