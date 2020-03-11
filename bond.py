H = 1000 # номинал облигации
c = 7 # доходность облигации
r = 6 # доходность ЦБ
n = 5 # лет
C = H * c / 100 # абсолюиное значение премии
m = 4 # количество выплат в год

fixed = H / ((1 + r / 100) ** n)
premium = 0
for i in range(1, n * m + 1):
    premium += (C / m) / ((1 + r / 100 / m) ** i)

price = fixed + premium

print("fixed:", fixed)
print("premium:", premium)
print("result:", price)

