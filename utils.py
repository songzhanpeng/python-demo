import json

def export_json_to_file(json_data, file_path):
    """
    将JSON数据导出到JSON文件

    Args:
        json_data (dict or list): 要导出的JSON数据。
        file_path (str): 目标JSON文件的路径。

    Returns:
        bool: 如果成功导出返回True，否则返回False。
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as json_file:
            # 使用json.dump将数据写入文件
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"导出JSON到文件时出现错误: {e}")
        return False

# 示例用法
json_data = {"name": "John", "age": 30, "city": "New York"}
file_path = "output.json"

if export_json_to_file(json_data, file_path):
    print(f"JSON数据已成功导出到文件 {file_path}")
else:
    print("导出JSON数据失败")


def write_string_to_file(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(data)
        print(f'已将数据写入到文件: {file_path}')
    except Exception as e:
        print(f'写入文件时发生错误: {str(e)}')

# # 使用示例
# icon_json_str = '...'  # 你的 JSON 字符串
# output_file_path = './icon_json.txt'
# write_string_to_file(icon_json_str, output_file_path)
