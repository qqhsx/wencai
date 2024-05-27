import pywencai
import os

# 获取关键字列表
keywords = os.environ.get("KEYWORDS", []).split(",")

# 遍历关键字列表进行查询和保存结果
for keyword in keywords:
    filename = f'{keyword}.csv'
    res = pywencai.get(question=keyword, loop=True)
    res.to_csv(filename, index=False, encoding='utf-8-sig')
    print(res)
