import datetime as date
from urllib.request import urlopen
from json import loads
import itertools

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
page_info = loads(urlopen(url).read().decode('utf8'))
revesions = sorted(page_info['query']['pages']['183903']['revisions'], key = lambda x : date.datetime.strptime(x['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date(), reverse = True)
revesions_groups = itertools.groupby(revesions, lambda x : date.datetime.strptime(x['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date())
res = {}
for info, group in revesions_groups:
    res[info] = list(group)
with open('revesions_statistics.txt', 'w', encoding='utf8') as file:
    for item in res:
        print(info, len(res[item]), file=file)
# Александр Градский умер 28.11 -> самое большое количество правок

