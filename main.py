import random

#Размеры матриц
size_stolbik = random.randint(4, 8)
size_strochka = random.randint(4, 8)

values = [-15, -4, -2, -7, 0, 3, 5, 12, 9] # Создание списка значений для матрицы

ne_three=[] #список с элементами не кратными 3

sum=0 

# Создание матрицы с рандомными элементами из нашего списка
matr = [[random.choice(values) for i in range(size_strochka)] for j in range(size_stolbik)]


for i in range(size_stolbik):# изображение матрицы
    for j in range(size_strochka):
        print(matr[i][j], end=' ')
    print()  # Переход на новую строку после каждой строки матрицы
     
 #цикл перебора строк матрицы, для нахождения и вывода элементов не кратным трем
for a in matr:
    for b in a:
        if b % 3 !=0 :
            ne_three.append(b)
print(f"список чисел ,которые не кратны трем {ne_three}")


#цикл перебрра элементов для рассчета суммы 
for num in ne_three:
    sum += num
print('Сумма чисел не кратных трем, равна: ',sum)     
     