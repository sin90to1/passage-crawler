'''
Author: Alex Shi
Date: 2023-04-11 22:49:37
LastEditTime: 2023-04-13 15:23:43
LastEditors: Alex Shi
Description: 
FilePath: /PassageCrawler/pipe/CetPassageCrawlerPipeline.py
'''
import time
from BaseSeleniumCrawlerPipeline import BaseSeleniumWebCrawler
from selenium.webdriver.common import by 

cet4BaseUrl = 'https://tiku.hujiang.com/subject/3/2?title=%E8%8B%B1%E8%AF%AD%E5%A4%A7%E5%AD%A6%E5%9B%9B%E7%BA%A7'
cet6BaseUrl = 'https://tiku.hujiang.com/subject/5/2?title=%E8%8B%B1%E8%AF%AD%E5%A4%A7%E5%AD%A6%E5%85%AD%E7%BA%A7'

class CetPassageCrawler(BaseSeleniumWebCrawler):
    def __init__(self, url) -> None:
        super().__init__(url)
    
    def locateElement(self, className):
        return self.driver.find_elements(by=by.By.CLASS_NAME, value=className)
    
    def autoFillingAnswer(self) -> None:
        return super().autoFillingAnswer()
    
    def run(self) -> None:
        self.openUrl(self.url)
        
    
