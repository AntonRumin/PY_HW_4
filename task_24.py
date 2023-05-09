'''
Задача 24: 
В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.

'''
print ('- - - Урожайность черники - - -')

def mass (length):
    print('Вводите значения урожайности каждого куста: ')
    array = list()
    i = 1
    while i < length + 1:
        a = int (input(f'Куст {i} имеет урожайность: '))
        array.append(a)
        i +=1
    print ('Ввод значений урожайности кустов окончен')
    print()
    return array

n = int(input('Введите число кустов на грядке: '))
gar_b = mass (n)
print (f'Урожайность кустов на грядке {gar_b}')

sum_maх = 0
# sum = 0

for i in range (n):

    if i == 0:
        sum_max = gar_b [n-1] + gar_b [0] +gar_b [1]
        sum = sum_max
    elif i == n-1:
        sum = gar_b [n-1] + gar_b [n-2] +gar_b [0]
    else:
        sum = gar_b [i-1] + gar_b [i] +gar_b [i+1]
        
    if sum > sum_max:
        sum_max = sum

print (f'Максимальное число ягод с трех кустов {sum_max}')
