from bs4 import BeautifulSoup
import requests as req

l = []
keywords = ['wwwiki']

x = 0
x1 = 0
e = 2.7

resp = req.get("http://kb.royal.co.ua/tag/%d0%b7%d1%83%d0%b1%d0%bd%d0%b0%d1%8f-%d1%84%d0%b5%d1%8f/")

info = BeautifulSoup(resp.text, 'lxml')

tags = info.find_all(['p'])[1:]

#strings = info.find_all(string=re.compile('text'))

for tag in tags:
    tmp = " ".join(tag.text.split('\n'))
    print(tmp)
    tmp_s = tmp.split(' ')
    result = list(set(keywords) & set(tmp_s))
    x = len(result)
    print(len(result))
    print(x)
    print(x1)
    if x > x1:
        x1 = x
    l.append(tmp)

y1 = 1/(1+e**(-x1))
print(y1)
