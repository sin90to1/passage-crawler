'''
Author: Alex Shi
Date: 2023-04-11 15:13:07
LastEditTime: 2023-04-11 22:53:17
LastEditors: Alex Shi
Description: 
FilePath: /PassageCrawler/pipe/BaseSeleniumCrawlerPipeline.py
'''
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium import webdriver
import abc
import time

class BaseSeleniumWebCrawler(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, url) -> None:
        self.url = url
        self.crawledContents = []
        
        options = Options()
        options.use_chromium = True
        options.add_argument('--disable-gpu')
        
        self.driver = webdriver.Edge(executable_path='home/alex/Edge Web Drive/msedgedriver', options=options)
    
    def openUrl(self, timeSleep):
        self.driver.execute_script(f'window.open("{self.url}");')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(timeSleep)
    
    @abc.abstractmethod
    def locateElement(self):
        return
    
    @abc.abstractmethod
    def autoFillingAnswer(self) -> None:
        return
    
    @abc.abstractmethod
    def run(self) -> None:
        return
    
    def getCrawedContents(self):
        return self.crawledContents
    
        
    
        
