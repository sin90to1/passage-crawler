'''
Author: Alex Shi
Date: 2023-04-08 21:33:13
LastEditTime: 2023-04-10 22:06:28
LastEditors: Alex Shi
Description: 
FilePath: /PassageCrawler/IeltsPassageCrawler.py
'''
from bs4 import BeautifulSoup
from collections import Iterable

import urllib
import requests
import re
import abc

headers = {
    'Cookie': 'Hm_lvt_80155549bc9515b10f24edf0c4637440=1679401154; taketest=1zqmt8ki; SSESS83cb9fb6134217f47c01ac2285e9d4ff=zbpDiURBuZU5VQse6zDEM2qM9uajhfZfirpaYQ7EWGQ',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51'
}

ieltsBaseUrl = "https://ieltsonlinetests.com/zh-hans/reading-test-collection"

class BaseCrawler(object):
    
    __metaclass__ = abc.ABCMeta
    def __init__(self, url, headers) -> None:
        self.url = url
        self.headers = headers
        self.crawledContents = None
    
    def get_html(self):
        html = requests.get(url=self.url, headers=self.headers).text
        self.parse_html(html)
    
    @abc.abstractmethod
    def _parseHtml(self, html):
        return
    
    def printElement(self):
        print(f'{self.__class__.__name__} running ...')
        if isinstance(self.crawledContents, Iterable):
            print(self.crawledContents[0])
        else:
            printDict = {key:value[0] for key, value in self.crawledContents.items()}
            print(printDict)
        print('Information Crawled. Sleep for 30 secs...')
    
    def getCrawledContents(self):
        return self.crawledContents
        

class MainPageCrawler(BaseCrawler):
    
    def __init__(self, url, headers) -> None:
        super().__init__(url, headers)
    
    def _parseHtml(self, html):
        soup = BeautifulSoup(html, 'lxml')
        self.crawledContents =  [item['href'] for item in soup.findAll('a', class_="ielts-volume__link")]


class PracticePageCrawler(BaseCrawler):
    
    def __init__(self, url, headers) -> None:
        super().__init__(url, headers)
    
    def _parseHtml(self, html):
        soup = BeautifulSoup(html, 'lxml')
        text_decription = soup.findAll('div', class_="passage-description")
        text_title = soup.findAll('h2', class_="subtitle")
        text_content = soup.findAll('div', class_="passage-content")
        text_questions = soup.find_all('div', class_="question question-1")
        self.crawledContents = {'general_question': [item.text for item in text_decription],
                                'passage_title': [item.text for item in text_title],
                                'raw_text': [item for item in text_content],
                                'raw_questions': [item for item in text_questions]
                                }


class SolutionPageCrawler(BaseCrawler):
    
    def __init__(self, url, headers) -> None:
        super().__init__(url, headers)
    
    def _parseHtml(self, html):
        soup = BeautifulSoup(html, 'lxml')
        self.crawledContents =  [item.text for item in soup.findAll('li', class_="list-answer-item")]


# This is only for test
def crawContents():
    soup = BeautifulSoup(open('./test/contents.html', 'r'), 'lxml')
    print(soup.findAll('a', class_="ielts-volume__link")[0]['href'])
    

def crawPractice():
    soup = BeautifulSoup(open('./test/practice.html', 'r'), 'lxml')
    text_decription = soup.findAll('div', class_="passage-description")
    text_title = soup.findAll('h2', class_="subtitle")
    text_content = soup.findAll('div', class_="passage-content")
    text_questions = soup.find_all('div', class_="question question-1")
    print(text_questions)

def crawSolutions():
    soup = BeautifulSoup(open('./test/practice.html'))
    solutions = soup.findAll('li', class_="list-answer-item")
    print(solutions)

if __name__=='__main__':
    crawContents()