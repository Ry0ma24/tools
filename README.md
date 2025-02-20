# tools

## split_markdown
这个 Python 脚本用于根据 Markdown 文件中的标题（一级或者二级 可自行修改‘#’的数量）将文件拆分成多个文件。每个拆分后的文件将包含标题和其下方的内容。这个工具适用于需要将大型 Markdown 文件按章节或部分分割成多个小文件的场景。

### 功能
按二级标题 (## ) 自动分割：脚本将按照 Markdown 文件中的一级标题来分割内容。
生成多个 Markdown 文件：每个拆分后的文件都将保留原始标题，并生成一个新的 .md 文件。
文件命名：拆分后的文件名将基于标题内容，并替换掉其中的空格，使用下划线 _ 替代。
### 要求
Python 3.x
无需额外安装第三方库
### 使用方法
克隆或下载此脚本到本地。
准备一个 Markdown 文件，确保它有明确的标题（例如 # Title 或 ## Title）。
将脚本与 Markdown 文件放在同一目录下。
