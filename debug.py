# DEBUG

from all_func import *

print("\nDEBUG")


str_1 = "10 2"
print(str_1)
print(set(str_1))
# str_shot = set(str_shot)
str_shot = [int(i) for i in str_1.split()]
print(str_shot)
print(set(str_shot))
print(str(range(11)))
print(set(range(11)))
print("num in 0-10?:", set(str_shot) < set(range(11)))
print({' '})

A = set([str(i) for i in range(10)]) | {' '}
print(A)
print("str_1 in set A?:", set(str_1) <= A)


