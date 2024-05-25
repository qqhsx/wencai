import pywencai
res = pywencai.get(question='退市股票', loop=True)
res.to_csv('问财.csv', index=False, encoding='utf-8-sig')
print(res)