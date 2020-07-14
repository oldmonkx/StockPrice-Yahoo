# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:09:06 2020

@author: Mayank T
"""


from bs4 import BeautifulSoup
import requests

url = input('Please enter Stock URL \n')

if url.split('/')[2] != 'in.finance.yahoo.com':
    print("Only in.finance.yahoo URL's accepted")
    url = input('Please enter Stock URL \n')
    
def price():
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    
    sensex = soup.find('div', class_='My(6px) Pos(r) smartphone_Mt(6px)')
    sensex_price = sensex.find('span').text
    return sensex_price



while True:
    print('The Current Stock Price is: ' + str(price()))




