import pywencai
import os

# 获取环境变量的值
keywords = os.environ.get("KEYWORDS", [])
# 将列表转换为字符串，使用逗号进行连接
keywords_str = ",".join(keywords)

# 检查关键字是否为空
if keywords_str:
    # 拆分关键字字符串为列表
    keywords = keywords_str.split(",")

    # 遍历关键字列表进行查询和保存结果
    for keyword in keywords:
        filename = f'{keyword}.csv'
        res = pywencai.get(question=keyword, loop=True)
        res.to_csv(filename, index=False, encoding='utf-8-sig')
        print(res)
else:
    print("No keywords found.")
