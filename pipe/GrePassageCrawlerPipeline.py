'''
Author: Alex Shi
Date: 2023-04-10 22:14:50
LastEditTime: 2023-04-11 23:23:29
LastEditors: Alex Shi
Description: 
FilePath: /PassageCrawler/pipe/GrePassageCrawlerPipeline.py
'''

import time
from BaseSeleniumCrawlerPipeline import BaseSeleniumWebCrawler
from selenium.webdriver.common import by 

contentUrl = "https://gre.kmf.com/practise/rc/159"

class GrePassageCrawler(BaseSeleniumWebCrawler):
    def __init__(self, url) -> None:
        super().__init__(url)
    
    def locateElement(self, className):
        return self.driver.find_elements(by=by.By.CLASS_NAME, value=className)
    
    def autoFillingAnswer(self) -> None:
        while True:
            optionBoxes = self.locateElement(className="inputRadio js-inputRadio")
            nextBoxes = self.locateElement(className="next js-next")
            if len(nextBoxes) == 0 and len(optionBoxes) == 0:
                return
            if len(nextBoxes) == 0:
                optionBoxes[0].click()
                nextBoxes[0].click()
                time.sleep(10)
    
    def run(self):
        self.openUrl(self.url, timeSleep=10)
        while True:
            passageBoxes = self.locateElement(className= "wl-cont js-link-jump")
            nextPageBoxes = self.locateElement(className="next")
            
            for passageBox in passageBoxes:
                passageUrl = passageBox.get_attribute("data-link").strip()
                self.openUrl(passageUrl, timeSleep=30)
                self.autoFillingAnswer()
                time.sleep(30)
                answerBoxes = self.locateElement(className="list-num g-clearfix")[0].find_elements(by=by.By.TAG_NAME, value="li")
                questionAnswerSet = None
                for answerBox in answerBoxes:
                    answerBox.click()
                    time.sleep(5)
                    questionAnswerSet = (
                        self.locateElement(className="question-info g-clearfix")[0],
                        self.locateElement(className="true-answer")[0]
                    )
                self.driver.close()
                self.crawledContents.append(questionAnswerSet)
            
            if len(nextPageBoxes) == 0:
                break
            else:
                nextPageBoxes[0].click()
                time.sleep(10)
    
                
                
                    
        
    
    
        
    

