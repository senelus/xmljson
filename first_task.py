import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

page_info = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(page_info)
res = []
for item in root.find('channel').findall('item'):
    pubDate_text = item.find('pubDate').text
    title_text = item.find('title').text
    dic = { 'pubDate': pubDate_text, 'title' : title_text }
    res.append(dic)
with open('news.json', 'w', encoding='utf8') as js:
    json.dump(res, js, indent = 1, ensure_ascii = False)