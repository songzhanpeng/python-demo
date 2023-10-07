import pandas as pd
import json
from utils import write_string_to_file
# 文件名
file_path = './iconandroid.xls'

# 读取Excel文件
xls = pd.ExcelFile(file_path)

# 获取所有工作表的名称
sheet_names = xls.sheet_names

# 创建一个空列表来存储工作表的JSON数据
json_data = []

# 循环遍历每个工作表并将其转换为JSON
for sheet_name in sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)
    # 将数据框（DataFrame）的数据转换为列表并添加到列表中
    json_data.extend(df.to_dict(orient='records'))

# 创建一个空字典来存储图标数据
icon_data = {}

# 循环处理每个数据项
for item in json_data:
    icon_name = item['图片名']
    icon_id = item['能力id']

    # 否则，创建一个新的图标条目
    icon_data[icon_id] = {
        "commandIcon": f'require("./white/{icon_name}.png")',
        "conditionIcon": f'require("./black/{icon_name}.png")',
        "name": icon_name,
    }

# 手动构建JSON字符串，包含JavaScript代码标记
icon_json_str = '{\n'
for icon_name, icon_info in icon_data.items():
    icon_json_str += f'    "{icon_name}": {{\n'
    icon_json_str += f'        "commandIcon": {icon_info["commandIcon"]},\n'
    icon_json_str += f'        "conditionIcon": {icon_info["conditionIcon"]},\n'
    icon_json_str += f'        "name": "{icon_name}",\n'
    icon_json_str += '    },\n'
icon_json_str += '}'

# 删除JavaScript代码标记并打印或保存JSON字符串
icon_json_str = icon_json_str.replace('"require(', 'require(').replace(')"', ')')
# print(icon_json_str)

write_string_to_file(icon_json_str, './icon.txt')
