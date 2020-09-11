n = 46
m = 32
i = 0
j = 0
NegativSumAll= 1
NegativSum = [0] * m
ifNegative = 0
countNegative = 0
NegativeModTwo = 1

a = []
for i in range(n):
    b = []
    for j in range(m):
        if i < 23: b.append(min(-n-i, m-j))
        if i > 22: b.append(max(-n-i, m-j))
        print("%3d" % b[j], end='')
    a.append(b)
    print(' |')

for i in range(m):
    print(" --", end='')
print()

for i in range(m):
    s = 0
    for j in range(n):

      if a[j][i] < 0: s += a[j][i]
    NegativSum[i] = s


for i in range(m):
    NegativSumAll *= NegativSum[i]

for i in range(m):
    for j in range(n):

      if a[j][i] > 0: ifNegative = 1
      else: ifNegative = 0

    if ifNegative == 0:
        countNegative +=1;

print('\n ☑ Произведение сумм отрицательных элементов каждого столбца:', NegativSumAll)

if countNegative > 0:
      print('\n ☑ Да, в матрице есть столбец/столбцы состоящие только из отрицательных чисел, их количество - ', countNegative)
else: print('\n ☒ В матрице нет столбцов, которые состоят только из отрицательных чисел')

for i in range(n):
    for j in range(m):
      if i % 2 != 0:
       if a[i][j] < 0:
           NegativeModTwo *= a[j][i]


print('\n ☑ Произведение отрицательных элементов матрицы, расположенных в строках с нечетными номерами:', NegativeModTwo)
input()