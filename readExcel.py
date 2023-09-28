import pandas as pd
from utils import export_json_to_file

# 打开Excel文件
file_path = './37新增能力0816_design_命名 (2).xlsx'
xls = pd.ExcelFile(file_path)

# 获取所有工作表的名称
sheet_names = xls.sheet_names

# 遍历每个工作表并将其转换为JSON
json_data = {}
for sheet_name in sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)
    json_data[sheet_name] = df.to_dict(orient='records')

# 打印JSON数据
print(json_data)
export_json_to_file(json_data, './xlsx.json')
