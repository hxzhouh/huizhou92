#!/bin/bash

# 遍历当前目录及子目录下所有 Markdown 文件
find . -type f -name "*.md" | while read -r file; do
  # 创建临时变量存储结果
  awk '
  {
    print $0  # 打印当前行

    # 如果当前行是 Gist 网址
    if ($0 ~ /^https:\/\/gist\.github\.com\/[a-zA-Z0-9_-]+\/[a-zA-Z0-9]+[[:space:]]*$/) {
      # 提取 Gist 用户名和 ID
      line = $0
      sub(/^https:\/\/gist\.github\.com\//, "", line)  # 去掉开头部分
      username = substr(line, 1, index(line, "/") - 1)  # 提取用户名
      gist_id = substr(line, index(line, "/") + 1)  # 提取 Gist ID

      # 检查是否已经插入了 {{< gist ... >}}
      getline next_line
      if (next_line !~ /{{< gist /) {
        # 插入格式化内容并保留下一行
        print "{{< gist " username " " gist_id ">}}"
        print next_line
      } else {
        # 如果已经有 {{< gist ... >}}，直接打印下一行
        print next_line
      }
    }
  }
  ' "$file" > "${file}.bak" && cat "${file}.bak" > "$file" && rm "${file}.bak"
done
