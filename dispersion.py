# -*- coding: utf-8 -*-

import math

# Дисперсия
# Есть две дискретные случайные величины с известными дисперсиями и корреляцией: D(x1) = 1, D(x2) = 2.25, rho(x1, x2) = 0.8
# Определите дисперсию суммы этих случайных величин D(x1+x2).

D1 = 1
D2 = 2.25
rho = 0.8

cov = rho * math.sqrt(D1 * D2)
D = D1 + D2 + 2 * cov
print(D)
