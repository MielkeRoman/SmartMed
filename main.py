import speech_recognition as sr
from urllib.request import urlopen
import os
import time
#import ukrfile


def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Добрий день, скажіть будь ласка в чому ваша проблема?")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            urlopen('http://google.com')
            print("Дякуємо, сервіси Google аналізують ваше запитання!")
            text = r.recognize_google(audio, language="ru-RU")
        except Exception:
            print("Дякуємо, йде аналіз вашого запитання!")
            text = r.recognize_sphinx(audio, language="ru-RU")
        finally:
            print(text)
    keywords = []
    with open('ukr_words.txt', encoding='windows-1251') as f:
        for line in f:
            for word in line.split():
                keywords.append(word.strip())
    f.close()
    t_word = text.split()
    result = list(set(keywords) & set(t_word))
    x = len(result)
    print(x)
    if x != 0:
        os.system('ukr_filesend.py')
        y = str(x)
        q = ("Iteration: " + y)
        f = open('statistics.txt', 'w')
        f.write(q)
        f.write('\n')
        f.write(text)
        f.close()
        time.sleep(1)
        os.system('statistic.py')
    else:
        os.system('rus_filesend.py')
        time.sleep(1)
        f = open('statistics.txt', 'w')
        f.write(text)
        f.close()
        time.sleep(1)
        os.system('statistic.py')
    os.system('analysis.py')


if __name__ == "__main__":
    main()
