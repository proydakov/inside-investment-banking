import math

# Квантиль
# С какой вероятностью среди 60-ти реализаций случайной величины будет ровно 3 значения, превышающих 95-ю квантиль? Ответ дайте целым числом процентов.

def soch(n, m):
    return math.factorial(n) / (math.factorial(n - m) * math.factorial(m))

res = 0.05 ** 3 * 0.95 ** 57 * soch(60, 3)
print(res)

