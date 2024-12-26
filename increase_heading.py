import os
import re

# 函数：将文件中的标题提升一级
def increase_all_headers(content):
    # 匹配以 '#' 开头的标题（H1, H2, H3, ...）
    def replace_header(match):
        header_level = match.group(1)
        
        # 提升所有标题级别（增加一个 #）
        new_header_level = '#' * (len(header_level) + 1)
        return new_header_level + match.group(2)

    # 使用正则表达式查找并修改标题
    return re.sub(r'^(#+)(.*)', replace_header, content, flags=re.MULTILINE)

# 函数：处理文件夹下的所有 Markdown 文件
def process_markdown_files(folder_path):
    # 遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 只处理扩展名为 .md 的文件（Markdown 文件）
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 检查文件中是否有 H1 标题
                if re.search(r'^# ', content, flags=re.MULTILINE):
                    # 如果有 H1 标题，则提升所有标题
                    new_content = increase_all_headers(content)
                    
                    # 如果内容有变更，则写回文件
                    if new_content != content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated: {file_path}")
                    else:
                        print(f"No changes needed: {file_path}")
                else:
                    print(f"No H1 header found, skipping: {file_path}")

# 主函数：指定要处理的文件夹路径（写死路径）
if __name__ == "__main__":
    folder_path = r"."  # 将这里的路径修改为你要处理的文件夹路径
    process_markdown_files(folder_path)
