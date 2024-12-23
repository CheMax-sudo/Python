# Функции.

#Алгоритм работы какой-либо логики заворачивают в функцию
#для того чтобы сократить объём кода и упростить его написание
#при дальнейшем повторении одинаковой части кода
#Функция может быть вызвана из других частей программы, при условии
#если она написана(создана) в начале хода обработки кода в верху
#или импортирована из библиотеки(каталога).
#Функция может принимать аргументы и возвращать значение.


#Цикл For
#Находим сумму всех чисел до переменной n 
# 5-->1+2+3+4+5=15
n = 5
x = 0
for n in range(1, n+1):
    x = x+n
#    print(x)
    
 
#Заворачиваем алоритм решения задачи в функцию для простоты вызова и чтобы не повоторять код
#Называем функцию summ
def summ(n):
    x = 0
    for n in range(1, n+1):
        x = x+n        
    return x

#Присваиваем переменной x результат вычисления фунуции summ       
#x = summ(5)
#print(x)       


#Цикл For
#Находим факториал числа n
#5-->1x2x6x24=120    
n = 5
f = 1
for i in range(2, n+1):
    f*=i

#print(f)
   

#Заворачиваем алоритм решения задачи в функцию для простоты вызова и чтобы не повоторять код
#Называем функцию fact

#====================================================== Функция возводит переменную в квадрат 
    
def square (x):
    print('Квадрат числа', x, '=',x**2)

#sqare()<--В скобках вводится аргумент, т.е. число которое необходимо возвести в квадрат

#Вызов цикла for для перебора функции и вызове её в каждом цикле, 10 итераций.
#for i in range(1,11):
#    square(i) 


#====================================================== Функция умножающая две переменные

def multiply(a,b):
    print(a*b)
  
    
#====================================================== Функция проверяющая на чётное и не чётное число 
   
def even(a):
    if a%2==0:
        print(a,'chetnoe')
    else:
        print(a,'nechetnoe')
        
        
#====================================================== Функция нахождения факториала

def fact(n):
    f = 1
    for i in range(2, n+1):
        f*=i
    return f

#print(fact(1))
  

#====================================================== Функция в условном операторе, приводится сравнение двух чисел  
  
if 5>6:
    def primer():
        print('первое число больше второго')
else:    
    def primer():
        print('первое число меньше второго') 
        

#====================================================== Функция создвёт рандомные элементы в списке, size вводится аргумент количества элементов

import random

def CreateList(size):
    list_1 = list()
    for i in range(size):
        rnd = random.randrange(1, 100)
        list_1.append(rnd)
    return list_1    
       
list_1 = CreateList(15) 
#print(list_1)   

#====================================================== Функция удаляет из списка необходимый элемент 

def DeleteListI(list): 
    print("Введите элемента который хотите удалить")
    n = int(input()) 
    for i in range(len(list)):
        if list[i] == n:
            list.pop(i)
            print(f'Элемент под номером {i+1} был успешно удалён!\n{list}')
            return list
    else:
        print("Такого элемента в списке нет")
        return list 
   
#====================================================== Функция добавляет в список элемент введёный пользователем. 
  
def AddElemList(list):         
    print("Введите значение элемента который хотите добавить:")
    elem = int(input())
    print("Теперь введите расположение элемента который хотите добавить:") 
    size = int(input())
    list.insert(size, elem)
    print(list)
    return list

#====================================================== Функция изменяет элемент списка на новый введёный пользователем.

def EditElemList(list):  
    print("Введите индекс элемента который хотите изменить:")
    size = int(input())
    print("Введите новое значение элемента:")
    newElem = int(input())
    list.pop(size)
    list.insert(size, newElem)
    return list  

#====================================================== Функция принимает аргументы кортежем, проверяет на тип введённых данных и суммирует

def check_args_type(*args): 
    for arg in args:
        if isinstance(arg, str):
            res = ''
            for i in args:
                res += i
            return res
        elif isinstance(arg, int):
            resDigits = 0
            for i in args:
                resDigits += i
            return resDigits
        else:
            print(f"Тип {type(arg)} не распознан.")  
            
#======================================================            
            
# Функция map() применяется для выполнения одной и той же функции
# над каждым элементом списка входных данных.     
  
#====================================================== Функция map() применяет стороннюю функцию для выполнения над каждым элементом списка.  

def square(x):    
  return x*2          # Возведение в квадрат(Суммируем на само себя) 
  #return x**2         # Возведения в степень(Умножаем на само себя)
  #return x%10         # Деление по остатку(Находим остаток от деления и получаем число от правого крайнего разряда)      
  #return x*-1         # Инверсирует полярность числа 
  
# x = map(square, ls)    # Функция map принимает в качестве аргументов функцию
#print(list(x))         # plus и список в котором необходимо каждый элемент 
                       # возвести в квадрат.

#====================================================== Создаёт словарь dict из кортежа tuple

def create_dict(a, b):
    return a, b

# функция `map()` останавливается, когда 
# заканчивается самая короткая последовательность
x = map(create_dict, ['a', 'b', 'c'], [3, 4, 5, 6])
#print(dict(x))
# {'a': 3, 'b': 4, 'c': 5}

#====================================================== Суммирует последовательности параллельно

def plus(a, b, c):
  return a + b + c

# функция 'plus' применяется (суммирует) к элементам 
# из всех последовательностей параллельно)
# 1+1+1
# 5+5+5

x = map(plus, [1, 5], [1, 5], [1, 5])
#print(list(x))
# [3, 15]

#====================================================== Возведение в степень

x = [3, 5, 6] 
y = [2, 2, 2]
# вычисление при помощи встроенной функции 'pow()' 
# 'x' в степени 'y' для каждого элемента 2-х списков
# x3 => y2
# x5 => y2
# x6 => y2 

ls = list(map(pow, x, y))
#print(ls)
# [9, 25, 36]

#====================================================== Подсчёт символов в элементе кортежа.

x = map(len, ('apple', 'banana', 'cherry'))
ls = list(x)
#print(ls)
# [5, 6, 6]

#====================================================== Создание словаря из двух списков. 

x = map(lambda *args: args, [1, 2], [3, 4])
dict1 = dict(x)
#print(dict1)
# {1: 3, 2: 4}

#====================================================== Удаление пунктуации в тексте при помощи map().

import re
def clean(word):
        return re.sub(r"[`!?.:;,'\"()-]", "", word.strip())

text = """С помощью цикла `for .. in:` программе 
необходимо хранить в памяти системы весь (список)! """
word = text.split()
word = map(clean, word)
text = ' '.join(word)
#print(text)
# 'С помощью цикла for  in программе необходимо 
# хранить в памяти системы весь список'

#====================================================== Метод split() в Python разделяет строку на список 'list' подстрок по разделителю. str.split(sep=None, maxsplit=-1)

a = 'Пример работы метода split'
#print(a.split())
# => ['Пример', 'работы', 'метода', 'split']

#====================================================== Функция калькулятор

def calculate(num1, operator, num2):
    if operator == '+':
        result = num1+num2
    elif operator == '-':
        result = num1-num2
    elif operator == '*':
        result = num1*num2
    elif operator == '/':
        if num2 != 0:
            result = num1/num2
        else:
            result = 'На ноль делить нельзя!'    
    else:
       print('Неверная операция!')
    return result

#num1 = int(input("Введите число:"))
#operator = input("Введите операцию:")
#num2 = int(input("Введите число:"))

#res = calculate(num1, operator, num2)
#print(res)  
            
#====================================================== Пузырьковая сортировка

def sort_list(list):
    n = len(list)
    tmp = 0
    j = 1
    for i in range(int(n)):
        for j in range(n-i):
            if list[i]>list[n-j-1]:
                tmp = list[i]
                list[i] = list[n-j-1]
                list[n-j-1] = tmp
    return list

#====================================================== Функция sorted() возвращает новый отсортированный список

str1 = "hello" 
list1 = ['one', 'two', 'list', '', 'dict']
tuple1 = (15, 3, 5, 7, 9, 11, 42)
tuple1 = [(1, 2), (11, 12), (0, 2), (3, 2)]
set1 = {1, 4, 3, 6, 2, 8, 11, 32}
dict1 = {2: 'red', 1: 'green', 3: 'blue'}

result = sorted(list1) # Сортирует в порядке возростания
result2 = sorted(list1, reverse=True) # Сортирует в порядке убвания
result3 = sorted(list1, key=len) # Сортирует с параметром key= функция с помощью которой выполниться сравнение
result4 = sorted(d1) # Вернется список отсортированных ключей
result5 = sorted(d1.values()) # Вернется список отсортированных значений
result6 = sorted(d1.values(), reverse=True) #Вернется список отсортированных значений c реверсом
result7 = sorted(d1.items()) # Вернется список кортежей (ключ, значение), отсортированный по ключам.

print(result7)
    
 
                    
    
   