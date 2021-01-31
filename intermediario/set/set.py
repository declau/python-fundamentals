# Intersection
{1, 2, 3, 4, 5}.intersection({3, 4, 5, 6})  # {3, 4, 5}
{1, 2, 3, 4, 5} & {3, 4, 5, 6}  # {3, 4, 5}

# Union
{1, 2, 3, 4, 5}.union({3, 4, 5, 6})  # {1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5} | {3, 4, 5, 6}  # {1, 2, 3, 4, 5, 6}

# Difference
{1, 2, 3, 4}.difference({2, 3, 5})  # {1, 4}
{1, 2, 3, 4} - {2, 3, 5}  # {1, 4}

# Symmetric difference with
{1, 2, 3, 4}.symmetric_difference({2, 3, 5})  # {1, 4, 5}
{1, 2, 3, 4} ^ {2, 3, 5}  # {1, 4, 5}

""" Let's say you've got a list of restaurants -- maybe you read it from a file. You care about the unique restaurants in
the list. The best way to get the unique elements from a list is to turn it into a set: """

restaurants = ["MacDonald's", "Burger King", "MacDonald's", "Chicken Chicken"]

unique_restaurants = set(restaurants)
print(unique_restaurants)


"""
Output: {'Chicken Chicken', "MacDonald's", 'Burger King'
 """
list(unique_restaurants)
# ['Chicken Chicken', "McDonald's", 'Burger King']
# Or
list(set(restaurants))
