from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1=Bar()
bar1.add_xaxis(["中國","日本","印度"])
bar1.add_yaxis("GDP", [40,20,3],     label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2=Bar()
bar2.add_xaxis(["中國","日本","印度"])
bar2.add_yaxis("GDP", [50,10,32],     label_opts=LabelOpts(position="right"))
bar2.reversal_axis()


bar3=Bar()
bar3.add_xaxis(["中國","日本","印度"])
bar3.add_yaxis("GDP", [70,40,36],     label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

timeline = Timeline({"theme":ThemeType})
timeline.add(bar1, "點1")
timeline.add(bar2, "點2")
timeline.add(bar3, "點3")

timeline.render("YY.html")