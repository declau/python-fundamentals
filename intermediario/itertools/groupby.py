from itertools import groupby


# def smaller_than_3(x):
#     return x < 3


a = [1, 2, 3, 4]
# group_obj = groupby(a, key=smaller_than_3)
group_obj = groupby(a, key=lambda x: x < 3)  # Lambda function

for key, values in group_obj:
    print(key, list(values))