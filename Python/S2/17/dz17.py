# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

num=int(input())
list_num=[random.randint(-num,num) for i in range(-num,num+1)]
print(list_num)

file = open('C:/Users/Sedov/Documents/GB/Python/S2/17/file.txt','r')
x= 1
for i in file:
    x*=list_num[int(i)]
    print(x)

