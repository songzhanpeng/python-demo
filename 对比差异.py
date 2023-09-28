import json

# 指定JSON文件路径
json_file_path = './excel.json'
json_file_path2 = './icons.json'

def read_json(file_path):
    # 使用with语句打开JSON文件并加载数据
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

# 调用read_json函数以获取JSON数据
data = read_json(json_file_path)
data2 = read_json(json_file_path2)

# 比较两个列表的差异
def compare_lists(list1, list2):
    common_elements = set(list1) & set(list2)
    different_elements = set(list1) ^ set(list2)
    
    return list(common_elements), list(different_elements)

# 调用比较函数
common_elements, different_elements = compare_lists(data, data2)

# 打印共同的元素
print("共同的元素:")
for element in common_elements:
    print(element)

# 打印不同的元素
print("\n不同的元素:")
for element in different_elements:
    print(element)

with open('different_elements.json', 'w') as json_file:
    json.dump(different_elements, json_file, indent=4)

print("icons.json 文件已创建")

