from pyecharts.charts import Line

line=Line()
line.add_xaxis(['中國','美國','日本'])
line.add_yaxis('GDP',[30,20,10])
line.render()