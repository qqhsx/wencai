import pywencai

# 定义变量
query = '退市股票'
# filename = f'{query}.csv'

# 使用变量进行查询和保存结果
res = pywencai.get(question=query, loop=True)
# res.to_csv(filename, index=False, encoding='utf-8-sig')

# 打印结果
print(res)
