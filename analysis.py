from bs4 import BeautifulSoup
import requests as req


def products(text):
    text = text.lower().split()
    wikies = ["%d1%81%d0%b5%d1%80%d0%b2%d0%b5%d1%80%d0%bd%d0%b0%d1%8f-%d1%87%d0%b0%d1%81%d1%82%d1%8c/",
              "%d0%b7%d0%b4%d0%be%d1%80%d0%be%d0%b2%d1%8c%d0%b5-%d0%bd%d0%b0%d1%86%d0%b8%d0%b8/",
              "%d0%b7%d1%83%d0%b1%d0%bd%d0%b0%d1%8f-%d1%84%d0%b5%d1%8f/", "ehealth_mis/"]
    soft = []
    for wiki in wikies:
        z = ('http://kb.royal.co.ua/tag/' + wiki)
        w = req.get(z)
        info = BeautifulSoup(w.text, 'lxml')
        tag = info.title.string.split('—')[0]
        soft.append({'tag': tag, 'len': len(list(set(text) & set(tag.lower().split())))})
    print(soft)

    x_max = max(map(lambda obj: obj['len'], soft))
    print(x_max)

    isEqual = all([obj['len'] == x_max for obj in soft])

    if isEqual == True:
        i = 0
        print('Нажаль не вдалося знайти відповідний продукт')
        for obj in soft:
            i = i+1
            print("{0} - {1}" . format(i, obj['tag']))
            y = (i, obj['tag'])
        x = int (input("Якщо Ваше запитання відноситься до роботи одного з вище вказаних ПЗ, оберіть відповідне йому значення! \n"
            "Якщо НІ - натиніть просто Enter: "))
        print(x)
        x -= 1
        i = 0
        while i<len(soft):
            i += 1
            if i == x:
                break
        print(soft[i])


        




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

