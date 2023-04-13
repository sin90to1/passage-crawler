'''
Author: Alex Shi
Date: 2023-04-11 15:59:52
LastEditTime: 2023-04-11 15:59:54
LastEditors: Alex Shi
Description: 
FilePath: /PassageCrawler/test/urlParseTest.py
'''
from urllib.parse import urljoin, urlparse, urlunparse, parse_qs, urlencode

content_url = "https://ieltsonlinetests.com/zh-hans/reading-test-collection"
passage_url = "/zh-hans/%E9%9B%85%E6%80%9D%E7%9C%9F%E9%A2%98%E8%AF%95%E5%8D%B7-%E4%B8%80%E6%9C%88-%E9%9B%85%E6%80%9D%E9%98%85%E8%AF%BB%E7%9C%9F%E9%A2%98-1-0"

# Remove the page argument from content_url
parsed_content_url = urlparse(content_url)
new_query = '&'.join([q for q in parsed_content_url.query.split('&') if not q.startswith('page=')])
new_parsed_content_url = parsed_content_url._replace(query=new_query)
new_content_url = urlunparse(new_parsed_content_url)

# Generate the complete URLs for passage_url and solution_url
complete_passage_url = urljoin(new_content_url, passage_url)
solution_url = urljoin(new_content_url, passage_url + "/solution")

print("Content URL:", new_content_url)
print("Passage URL:", complete_passage_url)
print("Solution URL:", solution_url)



