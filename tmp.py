def spider(j, i, text):

    l = []

    x = x1 = 0
    e = 2.7

    if i != None:
        resp = req.get(j)
        info = BeautifulSoup(resp.text, 'lxml')
        tags = info.find_all(['p'])[1:]
        for tag in tags:
            tmp = " ".join(tag.text.split('\n'))
            print(tmp)
            tmp_s = tmp.split(' ')
            result = list(set(text) & set(tmp_s))
            x = len(result)
            print(len(result))
            print(x)
            print(x1)
            if x > x1:
                print(x1)
                x1 = x
            l.append(tmp)
        y1 = 1 / (1 + e ** (-x1))
        print(y1)


def connect(j, text):
    from urllib.request import urlopen
    try:
        urlopen('http://google.com')
        i = urlopen('http://google.com')
    except Exception:
        i = None
    finally:
        if i == None:
            print('False')
            spider(j, i)
        else:
            print('True')
            spider(j, i, text)


def software(name_product, text):
    soft = {'Серверна частина': 'http://kb.royal.co.ua/tag/%d1%81%d0%b5%d1%80%d0%b2%d0%b5%d1%80%d0%bd%d0%b0%d1%8f-%d1%87%d0%b0%d1%81%d1%82%d1%8c/',
            "Здоров'я Нації": 'http://kb.royal.co.ua/tag/%d0%b7%d0%b4%d0%be%d1%80%d0%be%d0%b2%d1%8c%d0%b5-%d0%bd%d0%b0%d1%86%d0%b8%d0%b8/',
            'Зубна Фея': 'http://kb.royal.co.ua/tag/%d0%b7%d1%83%d0%b1%d0%bd%d0%b0%d1%8f-%d1%84%d0%b5%d1%8f/',
            'МІС eHealth': 'http://kb.royal.co.ua/tag/ehealth_mis/'}
    print(soft)
    print('Програмне забезпечення: ', name_product)
    for i in soft.items():
        if name_product in i:
            j = i[1]
            print(j)
    connect(j, text)



        #isEqual = input('Введіть')


    #software(name_product, text)


