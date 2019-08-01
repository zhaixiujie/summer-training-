
from collections import defaultdict, OrderedDict
import json
test_dict = {
    'name': 'fang',
    'age': 12,
    'sex':'male'
}
json_str = json.dumps(test_dict, indent=4)   #json.dumps将字典转换为字符串
with open('test_data.json', 'w') as json_file:
    json_file.write(json_str)
