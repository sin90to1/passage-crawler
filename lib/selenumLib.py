'''
Author: Alex Shi
Date: 2023-04-08 13:23:52
LastEditTime: 2023-04-11 15:12:03
LastEditors: Alex Shi
Description: 
FilePath: /PassageCrawler/lib/selenumLib.py
'''
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium import webdriver


def initialize():
    options = Options()
    options.use_chromium = True
    options.add_argument('--disable-gpu')
    
    driver = webdriver.Edge(executable_path='home/alex/Edge Web Drive/msedgedriver', options=options)
    return driver