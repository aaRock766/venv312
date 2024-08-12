# -*- coding:utf-8 -*-
<<<<<<< HEAD
import pyecharts
from pyecharts.charts import Line
from pyecharts.options import TitleOpts
line=Line()
line.add_xaxis(["中國","美國","法國"])
line.add_yaxis("GDP",[30,10,20])


line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="2%")
)


line.render()
=======
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
>>>>>>> c7e04b19472760108cd584319db2b8c4b6ea244b
