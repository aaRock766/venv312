# -*- coding:utf-8 -*-
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