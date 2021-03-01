from itertools import accumulate
import operator

a = [1, 2, 3, 4]

acc = accumulate(a)
print(a)
print(list(acc))  # plus the elements

acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))  # multiply the elements
