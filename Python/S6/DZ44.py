# 44. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

a=[int(input(f"Введите {i} координату тучки A ")) for i in "xy"]
b=[int(input(f"Введите {i} координату тучки B ")) for i in "xy"]

result = round(sum([(coordinate[1]-coordinate[0])**2 for coordinate in zip(a,b)])**0.5,3)
print(f'A {a},B {b}-> {result}')
