import os
import json

# 指定要读取的文件夹路径
folder_path = './黑'


image_files = []

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查文件扩展名是否为图片格式（可以根据需要添加更多扩展名）
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
        # 如果是图片文件，将其添加到list中，以文件名作为键
        image_files.append(filename)

# 将list保存为JSON文件
with open('icons.json', 'w') as json_file:
    json.dump(image_files, json_file, indent=4)

print("icons.json 文件已创建")
