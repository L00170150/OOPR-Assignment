"""
#
# File     :L00170150_Q2.py
# created  : 28/11/2021 20:34
# Author   : Neha Tripathi
# Version  :v1.0.0
# Licencing : 2021 Neha Tripathi
# Description : Find all the headings on Apache 2 web page  using lxml parser
to find the apache2 word in a webpage and to count it
Find the title of webpage
#
"""
from bs4 import BeautifulSoup
import requests
import re

source = requests.get('http://192.168.43.128/').text

soup = BeautifulSoup(source, 'lxml')

tag = soup.find('title')   # This will give the title of the Apache2 Page
print(tag.text)

for match in soup.find_all('div',class_='section_header'):   # For loop to find all the headers on the Page
    header = match.text
    print(header)



count = len(soup.find_all(text=re.compile("apache2"))) +  len(soup.find_all(text=re.compile("Apache2")))
print('\nUrl: http://192.168.43.128/ contains {} occurrences of word apache2'.format(count))



