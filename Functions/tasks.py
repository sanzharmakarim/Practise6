#task1
nums = [1, 2, 3, 4, 5, 6, 7, 8]
res_1 = list(map(lambda x: x ** 2, nums))
res_2 = list(filter(lambda x: x % 2 == 0, nums))
print(res_1)
print(res_2)

#task2
from functools import reduce
nums = [1, 2, 3, 4]
res = reduce(lambda x, y: x + y, nums)
print(res)

#task3
names = ["Steve", "Arthur", "Artyom", "John"]
ages = [34, 36, 30, 38]
for index, val in enumerate(names, start=1):
    print(index,val)
paired = list(zip(names, ages))
print(paired)

#task4
num = 20
print(type(num))
print(isinstance(num, int))
x = "123"
num = int(x)
flt = float(x)
l = list("abc")
print(num)  
print(flt)   
print(l)  
