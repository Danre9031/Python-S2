# 45. Найти сумму чисел списка стоящих на нечетной позиции

num_les=[1,4,5,6,2]
print(num_les)
result=sum([val for ind,val in enumerate(num_les) if ind%2==1])
print(result)