'''
Author: Alex Shi
Date: 2023-04-10 20:08:08
LastEditTime: 2023-04-11 22:46:11
LastEditors: Alex Shi
Description: 
FilePath: /PassageCrawler/main.py
'''
import pipe.IeltsPassageCrawlerPipeline as IeltsPassageCrawlerPipeline
import pipe.GrePassageCrawlerPipeline as GrePassageCrawlerPipeline
import time
import json

from urllib.parse import urlparse, parse_qs, urlencode, urlunparse, urljoin

class mainClass(object):
    
    def __init__(self, type) -> None:
        self.type = type
        self.crawledObj = []
    
    def execute(self):
        if self.type=='ie':
            ieltsHeaders = IeltsPassageCrawlerPipeline.headers
            baseUrl = IeltsPassageCrawlerPipeline.ieltsBaseUrl
            allContentPages = ['0','1']
            for page in allContentPages:
                parsedUrl = urlparse(baseUrl)
                urlToModify = parse_qs(parsedUrl)
                urlToModify['page'] = [page]
                ieltsUrl = urlunparse(parsedUrl._replace(query=urlencode(urlToModify, doseq=True)))
                
                contentCrawler = IeltsPassageCrawlerPipeline.MainPageCrawler(url=ieltsUrl, headers=ieltsHeaders)
                passageUrls = contentCrawler.get_html()
                contentCrawler.printElement()
                time.sleep(30)
                
                for passageUrlSuffix in passageUrls:
                    newBaseUrl = urlunparse(parsedUrl._replace(query='&'.join([q for q in parsedUrl.query.split('&') if not q.startswith('page=')])))
                    passageUrl = urljoin(newBaseUrl, passageUrlSuffix)
                    solutionUrl = urljoin(newBaseUrl, passageUrlSuffix + "/solution")
                    
                    passageCrawler = IeltsPassageCrawlerPipeline.PracticePageCrawler(url=passageUrl, headers=ieltsHeaders)
                    passageCrawler.get_html()
                    passageCrawler.printElement()
                    time.sleep(30)
                    
                    solutionCrawler = IeltsPassageCrawlerPipeline.SolutionPageCrawler(url=solutionUrl, headers=ieltsHeaders)
                    solutionCrawler.get_html()
                    solutionCrawler.printElement()
                    time.sleep(30)
                    
                    self.crawledObj.append((passageCrawler.getCrawledContents(), solutionCrawler.getCrawledContents()))
        elif self.type=='gr':
            # TODO: Other passage crawling.
            greCrawler = GrePassageCrawlerPipeline.GrePassageCrawler(GrePassageCrawlerPipeline.contentUrl)
            greCrawler.run()
            self.crawledObj = greCrawler.getCrawedContents()
    
    def storeAsRawJson(self):
        if self.type=='ie':
            basePath = './data/IELTS Passages/raw data/'
        elif self.type=='ge':
            basePath = './data/GRE Passages/raw data/'
        for id, element in enumerate(self.crawledObj):
            fileName = basePath + f"raw_exercise_{str(id)}.json"
            with open(fileName, 'w+') as fw:
                json.dump(list(element))
                
            
                
                


                    
                    
                    