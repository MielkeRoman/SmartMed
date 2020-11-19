import os.path

files = ["products/Серверна частина.txt", "products/Здоров'я Нації.txt",
             "products/Зубна Фея.txt", "products/МІС eHealth.txt"]

for file in files:
    f = open(file, "r", encoding="utf-8")
    file = os.path.splitext(os.path.basename(file))[0]
    print(file)