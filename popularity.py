import os
import pywencai

try:
    # 进行查询并获取结果
    res = pywencai.get(question='人气排名', loop=True)
    if res is None:
        raise ValueError("Did not receive any data. The result is None.")
    
    # 预处理数据以匹配需要的格式
    processed_data = []
    for index, row in res.iterrows():
        code = str(row['股票代码'])
        if code.startswith(('000', '001', '002', '003', '300', '301', '200')):
            market = '0'
        elif code.startswith(('600', '601', '603', '605', '688', '689', '900')):
            market = '1'
        elif code.startswith(('8', '4')):
            market = '2'
        else:
            market = '未知'
        stock_code = row['股票代码']
        data_number = '1'  # 假定这里你想写入非9的任何数字，例如1
        string_value = str(index + 1)
        numeric_value = string_value
        line = '|'.join([market, stock_code, data_number, string_value, numeric_value])
        processed_data.append(line)
    
    # 保存数据到 extern_user.txt 文件
    txt_path = 'extern_user.txt'
    with open(txt_path, 'w', encoding='utf-8') as f:
        for line in processed_data:
            f.write(line + '\n')

except Exception as e:
    print(f"An error occurred: {e}")