import datetime as date
from urllib.request import urlopen
from json import loads
import itertools

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
page_info = loads(urlopen(url).read().decode('utf8'))
revesions = sorted(page_info['query']['pages']['192203']['revisions'], key = lambda x : date.datetime.strptime(x['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date(), reverse = True)
revesions_groups = itertools.groupby(revesions, lambda x : date.datetime.strptime(x['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date())
res = {}
for info, group in revesions_groups:
    res[info] = list(group)
with open('revesions_statistics1.txt', 'w', encoding='utf8') as file:
    for item in res:
        print(info, len(res[item]), file=file)

# 15.12.2007 писатель умер -> больше всего правок, но такая метрика не всегда имеет место быть, поскольку у более популярных страниц может быть гораздо больше правок в связи с другими "громкими событиями"