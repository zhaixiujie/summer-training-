import csv

data = [[u'姓名'+' '+u'年龄'+' '+u'性别'],
        [u'张三'+'  '+u'12'+'   '+u'男'],
        [u'李四'+'  '+u'13'+'   '+u'男'],
        [u'嘻嘻'+'  '+u'15'+'   '+u'女'],
        [u'小明'+'  '+u'10'+'   '+u'男'],
        [u'小花'+'  '+u'12'+'   '+u'女']]

with open('results.csv','w',newline='',encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerows(data)