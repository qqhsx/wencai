import os
import pywencai

# 从环境变量读取查询词
query = os.getenv('CSV_FILE_NAME ', '退市股票')  # 如果环境变量不存在，则使用默认值 '退市股票'
filename = f'{CSV_FILE_NAME }.csv'

# 使用变量进行查询和保存结果
res = pywencai.get(question=query, loop=True)
res.to_csv(filename, index=False, encoding='utf-8-sig')

# 打印结果
print(res)
