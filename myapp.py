#zundoko
import random

MESSAGE = 'ズンズンズンズンドコ'

list = []
while ''.join(list[-5:]) != MESSAGE:
    list.append(random.choice(['ズン', 'ドコ']))
    print(list[-1])
print('キ・ヨ・シ！')