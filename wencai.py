import pywencai
import os
import pandas as pd  # 导入 pandas 库

# 获取关键字列表
# 在Settings-Actions中创建一个New repository secret，名称为“KEYWORD”。秘密为"人气排名,涨停,退市股票"
keywords = os.environ.get("KEYWORD", "").split(',')

# 遍历关键字列表进行查询和保存结果
for keyword in keywords:
    filename = f'{keyword}.csv'
    res = pywencai.get(question=keyword, loop=True)
    
    # 将 res 转换为 DataFrame 对象
    if isinstance(res, dict):
        res = pd.DataFrame(res)
    
    # 确保 res 现在是 DataFrame
    if not isinstance(res, pd.DataFrame):
        print(f"Error: Expected DataFrame, got {type(res)}")
        continue
    
    # 保存到 CSV 文件
    res.to_csv(filename, index=False, encoding='utf-8-sig')
    print(res)
