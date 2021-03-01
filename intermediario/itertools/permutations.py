from itertools import permutations, combinations_with_replacement

a = [1, 2, 3]

perm = permutations(a)
print(list(perm))


perm = permutations(a, 2)
print(list(perm))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))
