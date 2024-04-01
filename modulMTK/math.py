import math

#konstanta
print('pi =', math.pi)
print('e =', math.e)

#faktorial, n!
for i in range(1, 11):
    print('{}! = {}'.format(i, math.factorial(i)))
    print('%s! = %s' % (i, math.factorial(i)))

#pangkat
print('2 pangkat 3 =', math.pow(2, 3))

#akar kuadrat
print('akar kuadrat dari 16 =', math.sqrt(16))

#logarithm
print('logaritma basis 10 dari 100 =', math.log(100, 10))
print('log 8 = ', math.log(8))
print('log 8 basis 2 = ', math.log2(8))

#trigonometri
print('sin 90 derajat =', math.sin(math.radians(90)))