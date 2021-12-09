import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

page_info = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(page_info)
res = []
for item in root.find('channel').findall('item'):
    dic = {}
    for child in item:
        dic[child.tag] = child.text
    res.append(dic)
with open('news1.json', 'w', encoding='utf8') as js:
    json.dump(res, js, indent=1, ensure_ascii=False)
