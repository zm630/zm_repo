import json
import pyecharts.options as opts
from pyecharts.charts import Line
'''
疫情案例可视化
'''
#加载数据
india_data=open("印度.txt","r",encoding="utf-8").readlines()
usa_data=open("美国.txt","r",encoding="utf-8").readlines()
jap_data=open("日本.txt","r",encoding="utf-8").readlines()
# print(india_data)
# print(usa_data)
# print(jap_data)
#解析数据
#获取x轴   共享x轴，只需要获取一次数据
india_data=india_data[0].replace("jsonp_1629350745930_63180(","")[:-2]
usa_data=usa_data[0].replace("jsonp_1629344292311_69436(","")[:-2]
jap_data=jap_data[0].replace("jsonp_1629350871167_29498(","")[:-2]

india_data_dict = json.loads(india_data)
usa_data_dict = json.loads(usa_data)
jap_data_dict = json.loads(jap_data)
india_x_day = india_data_dict["data"][0]['trend']['updateDate'][0:365]
# print(india_x_day)

#获取y轴
india_y_data = india_data_dict['data'][0]['trend']['list'][3]['data'][0:365]
usa_y_data = usa_data_dict['data'][0]['trend']['list'][3]['data'][0:365]
jap_y_data = jap_data_dict['data'][0]['trend']['list'][3]['data'][0:365]


#生成图表


"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=line-stack

目前无法实现的功能:

暂无
"""




(
    Line()
    .add_xaxis(xaxis_data=india_x_day)
    .add_yaxis(
        series_name="印度新增感染人数",
        stack="总量",
        y_axis=india_y_data,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="美国新增感染人数",
        stack="总量",
        y_axis=usa_y_data,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="日本新增感染人数",
        stack="总量",
        y_axis=jap_y_data,
        label_opts=opts.LabelOpts(is_show=False),

    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="折线图堆叠"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    .render("基于折线图的疫情案例实现.html")
)
