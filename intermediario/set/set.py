""" Let's say you've got a list of restaurants -- maybe you read it from a file. You care about the unique restaurants in
the list. The best way to get the unique elements from a list is to turn it into a set: """

restaurants = ["MacDonald's", "Burger King", "MacDonald's", "Chicken Chicken"]

unique_restaurants = set(restaurants)
print(unique_restaurants)


""" 
Output: {'Chicken Chicken', "MacDonald's", 'Burger King'
 """
