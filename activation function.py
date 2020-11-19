text = ('Моя програма мой не працюе тому що...')

e = 2.7

keywords = []
with open('ukr_words.txt', encoding='windows-1251') as f:
    for line in f:
        #for word in line.split('=>' and ','):
        for word in line.split():
            keywords.append(word.strip())
print(keywords)

t_word = text.split()
print(t_word)

result=list(set(keywords) & set(t_word))
print(len(result))
x1 = len(result)
print(x1)
y1 = 1/(1+e**(-x1))
print(y1)


keywords = []
with open('rus_words.txt', encoding='windows-1251') as f:
    for line in f:
        for word in line.split():
            keywords.append(word.strip())
print(keywords)

t_word = text.split()
print(t_word)

result=list(set(keywords) & set(t_word))
print(len(result))
x2 = len(result)
print(x2)
y2 = 1/(1+e**(-x2))
print(y2)