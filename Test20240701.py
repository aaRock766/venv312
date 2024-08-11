# -*- coding:utf-8 -*-
<<<<<<< HEAD
fr = open('14.txt','r',encoding='UTF-8')
# content = f.read()
# print(content)
for line in fr:
    line = line.strip()
    t = line.split(",")[-1]
    if t == '正式':
        fw =open('14.txt.bak','a',encoding='Utf-8')
        fw.write(line+'\n')
    else:
        continue
fr.close()
fw.close()
=======
from time import sleep
print("su")
time.sleep(5)
print("aa")
>>>>>>> 013c6cd552a9222c38be5c47b60378c15a680151
