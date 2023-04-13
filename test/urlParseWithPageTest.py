'''
Author: Alex Shi
Date: 2023-04-11 16:01:03
LastEditTime: 2023-04-11 16:01:04
LastEditors: Alex Shi
Description: 
FilePath: /PassageCrawler/test/urlParseWithPageTest.py
'''
from urllib.parse import urljoin, urlparse, urlunparse, parse_qs, urlencode

baseUrl = "https://ieltsonlinetests.com/zh-hans/reading-test-collection"
allContentPages = ['0', '1']
for page in allContentPages:
    parsedUrl = urlparse(baseUrl)
    urlToModify = parse_qs(parsedUrl.query)
    urlToModify['page'] = [page]
    ieltsUrl = urlunparse(parsedUrl._replace(query=urlencode(urlToModify, doseq=True)))
    print(f'The URL of page {page} is {ieltsUrl}')