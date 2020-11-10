def spider(j, i, text):
    from bs4 import BeautifulSoup
    import requests as req

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


def software(name_file, text):
    soft = {'Серверна частина': 'http://kb.royal.co.ua/tag/%d1%81%d0%b5%d1%80%d0%b2%d0%b5%d1%80%d0%bd%d0%b0%d1%8f-%d1%87%d0%b0%d1%81%d1%82%d1%8c/',
            "Здоров'я Нації": 'http://kb.royal.co.ua/tag/%d0%b7%d0%b4%d0%be%d1%80%d0%be%d0%b2%d1%8c%d0%b5-%d0%bd%d0%b0%d1%86%d0%b8%d0%b8/',
            'Зубна Фея': 'http://kb.royal.co.ua/tag/%d0%b7%d1%83%d0%b1%d0%bd%d0%b0%d1%8f-%d1%84%d0%b5%d1%8f/',
            'МІС eHealth': 'http://kb.royal.co.ua/tag/ehealth_mis/'}
    print(soft)
    print('Програмне забезпечення: ', name_file)
    for i in soft.items():
        if name_file in i:
            j = i[1]
            print(j)
    connect(j, text)


def products(text):
    text = text.lower().split()
    files = ["products/Серверна частина.txt", "products/Здоров'я Нації.txt",
             "products/Зубна Фея.txt", "products/МІС eHealth.txt"]
    soft = []
    for file in files:
        f = open(file, "r", encoding="utf-8")
        soft.append({'file': file, 'len': len(list(set(text) & set(f.read().lower().split())))})
    print(soft)

    x_max = max(map(lambda obj: obj['len'], soft))

    print(x_max)

    isEqual = all([obj['len'] == x_max for obj in soft])

    print(isEqual)

    if isEqual:
        print('Сформулюйте будь ласка більш чітко питання!')
        from sys import exit
        exit()

    else:
        import os.path

    for obj in soft:
        if obj['len'] == x_max:
            #name_file = obj['file']
            # print(os.path.splitext(os.path.basename(path_file))[0])
            print(os.path.splitext(os.path.basename(obj['file']))[0])
            name_file = os.path.splitext(os.path.basename(obj['file']))[0]
    print(name_file)
    software(name_file, text)


def main():
    try:
        f = open("statistic.txt")
        text = f.read().split('\n\n')[1]
        f.close()
        print(text)
        if len(text) < 8:
            text = input("Введіть Ваше запитання або помилку на екрані: ")
    except Exception:
        g = "Error File!!!"
        print(g)
        text = input("Введіть Ваше запитання або помилку на екрані: ")

    products(text)


if __name__ == "__main__":
    main()

