from bs4 import BeautifulSoup
import requests as req


def products(text):
    text = text.lower().split()
    wikies = ["%d1%81%d0%b5%d1%80%d0%b2%d0%b5%d1%80%d0%bd%d0%b0%d1%8f-%d1%87%d0%b0%d1%81%d1%82%d1%8c/",
              "%d0%b7%d0%b4%d0%be%d1%80%d0%be%d0%b2%d1%8c%d0%b5-%d0%bd%d0%b0%d1%86%d0%b8%d0%b8/",
              "%d0%b7%d1%83%d0%b1%d0%bd%d0%b0%d1%8f-%d1%84%d0%b5%d1%8f/", "ehealth_mis/"]
    soft = []
    x = 0
    i = 0
    y = 0
    for wiki in wikies:
        z = ('http://kb.royal.co.ua/tag/' + wiki)
        w = req.get(z)
        info = BeautifulSoup(w.text, 'lxml')
        tag = info.title.string.split('—')[0]
        soft.append({'tag': tag, 'len': len(list(set(text) & set(tag.lower().split())))})
        print(soft)

        x_max = max(map(lambda obj: obj['len'], soft))
        print(x_max)
        for obj in soft:
            if obj['len'] == x_max:
                name_product = (obj['tag'])
                print('Програмний продукт: ', name_product)

        isEqual = all([obj['len'] == x_max for obj in soft])

        if isEqual == True:
            soft = {}
            i = 0
            print('Нажаль не вдалося знайти відповідний продукт')
            for wiki in wikies:
                i = i + 1
                z = ('http://kb.royal.co.ua/tag/' + wiki)
                w = req.get(z)
                info = BeautifulSoup(w.text, 'lxml')
                tag = info.title.string.split('—')[0]
                soft[i] = tag
            for item in soft.items():
                print(item)
            x = int(input(
                "Якщо Ваше запитання відноситься до роботи одного з вище вказаних ПЗ, оберіть відповідне йому значення! \n"
                "Якщо НІ - натиніть просто Enter: "))
            print(x)
            x -= 1
            i = 0
            print(soft)




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

