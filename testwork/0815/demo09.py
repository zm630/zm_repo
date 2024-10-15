#1.加载数据
import json
from pyecharts import options as opts
from pyecharts.charts import Map

nationwide_data = open("疫情.txt","r",encoding="utf-8").read()
#2.获取数据
nationwide_data_dict = json.loads(nationwide_data)
city_data = nationwide_data_dict['areaTree'][0]['children']
#3.封装数据
province_data = []
sichuan_data_dict = dict()
#4.组装数据
for data in city_data:
    print("------------------------------------------------------------------------------------>")
    if(data['name'] == '四川'):
        sichuan_data_dict = data
for index in range(1,len(sichuan_data_dict['children'])):
    data_tuple = (sichuan_data_dict['children'][index]['name'] + "市",sichuan_data_dict['children'][index]['total']['confirm'])
    province_data.append(data_tuple)
print(province_data)
"""
  {'name': '成都', 'today': {'confirm': 0, 'confirmCuts': 0, 'isUpdated': False}, 'total': {'nowConfirm': 4, 'confirm': 163, 'suspect': 0, 'dead': 3, 'deadRate': '1.84', 'showRate': False, 'heal': 156, 'healRate': '95.71', 'showHeal': True, 'grade': '全部低风险', 'wzz': 0}}
"""

#4.构建地图
c = (
    Map()
    .add("新冠疫情实时情况", province_data,"四川")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-四川省新冠确诊人数"),
        visualmap_opts=opts.VisualMapOpts(
            pieces = [
                    {"min": 1, "max": 30, "label": '1-2000', "color": "red"},
                    {"min": 30, "max": 60, "label": '2000-5000', "color": "green"},
                    {"min": 60, "max": 100, "label": '5000-10000', "color": "yellow"},
                    {"min": 100, "max": 200, "label": '10000-20000', "color": "blue"},
                ]
            )
    )
    .render("3.基于Map呈现四川各城市新冠确诊人数.html")
)
