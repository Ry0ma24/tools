import os

def split_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 按照二级标题 (即 ## 分割内容
    sections = content.split('\n## ')
    sections[0] = sections[0].lstrip('## ')  # 去掉文件开头的 '# '

    # 创建分割后的文件
    for i, section in enumerate(sections):
        if section.strip():  # 如果章节非空
            title = section.split('\n')[0]  # 获取标题
            title = title.strip().replace(' ', '_')  # 用下划线代替空格
            file_name = f"{i+1}_{title}.md"
            
            with open(file_name, 'w', encoding='utf-8') as out_file:
                out_file.write('## ' + section)

            print(f"Created {file_name}")

if __name__ == '__main__':
    split_markdown('README.md') # 修改
