# -*- coding:utf-8 -*-
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