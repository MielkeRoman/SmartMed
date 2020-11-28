from bs4 import BeautifulSoup
import requests as req

text = 'Фея'
text = text.lower().split()
wikies = ["%d1%81%d0%b5%d1%80%d0%b2%d0%b5%d1%80%d0%bd%d0%b0%d1%8f-%d1%87%d0%b0%d1%81%d1%82%d1%8c/",
              "%d0%b7%d0%b4%d0%be%d1%80%d0%be%d0%b2%d1%8c%d0%b5-%d0%bd%d0%b0%d1%86%d0%b8%d0%b8/",
              "%d0%b7%d1%83%d0%b1%d0%bd%d0%b0%d1%8f-%d1%84%d0%b5%d1%8f/", "ehealth_mis/"]
soft = []
i = 0
for wiki in wikies:
    i = i + 1
    z = ('http://kb.royal.co.ua/tag/' + wiki)
    w = req.get(z)
    info = BeautifulSoup(w.text, 'lxml')
    tag = info.title.string.split('—')[0]
    soft.append({'tag': tag, 'len': len(list(set(text) & set(tag.lower().split()))), 'i': i})
print(soft)

x_max = max(map(lambda obj: obj['len'], soft))
print(x_max)