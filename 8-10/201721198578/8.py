# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:32:11 2017

@author: si qi
"""

#统计字数
def get_ch_table(line):
    ch_table = []
    for ch in line:
        if ch not in ch_table:
            ch_table.append(ch)
    return ch_table

# 主程序
fh = open(r'F:\homework\codes-python\poem.txt')
text = fh.read()
poem1 = text.replace('\n', '') 
#总字表
chs = get_ch_table(poem1)
#print(len(chs), chs)
#print(text)

poem2 = poem1.replace('，','')
poem3 = poem2.replace('。','\n')
print(poem3)
fh = open(r'F:\homework\codes-python\poem_correct.txt', 'w')
for idiom in poem3:
    fh.write(idiom)
fh.close()

import random
poem4 = poem3.split()
choice_poem = random.choice(poem4)
print(choice_poem)
#print(choice_poem[1])

guess_ch_table = [ch for ch in choice_poem]
print(guess_ch_table)
while len(guess_ch_table) < 12:
    ch = random.choice(chs)
    if ch not in guess_ch_table:
        guess_ch_table.append(ch)

random.shuffle(guess_ch_table)

for i in range(0,12,2):
    print(guess_ch_table[i], guess_ch_table[i+1])