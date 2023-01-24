# 46.Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)

num_les=[1,4,5,6,2]
print(num_les)
result=[num_les[ind]*num_les[-ind-1] for ind in range(len(num_les)//2+len(num_les)%2)]
print(result)