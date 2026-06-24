import functools
import math

NAME_INDEX = 0
CATEGORY_INDEX = 1
PRICE_INDEX = 2

category_types = ['Clothing', 'Shoes', 'Bicycle', 'Accessories']

shopping_list = [
    ["Bib Shorts", "Clothing", 92.50],
    ["Roubaix", "Bicycle", 3599.99],
    ["Cycling computer", "Accessories", 394.99],
    ["Helmet", "Accessories", 299.99],
    ["Road Shoes", "Shoes", 144.99],
    ["700c presta tube", "Accessories", 5.25],
    ["Jersey", "Clothing", 25.99],
    ["Multi-Function Tool", "Accessories", 22.99],
    ["Gloves", "Accessories", 8.99],
    ["Cleats", "Shoes", 15.99],
    ["Power Pedals", "Accessories", 999.99],
    ["Socks", "Clothing", 8.50]
]

# list items in each category

for category in category_types:
    category_list = list(filter(lambda item : item[CATEGORY_INDEX] == category, shopping_list))
    print(category)
    for item in category_list:
        print(f'\t{item}')

# find the total cost

# use map to creat a list of just the cost
cost_list = list(map(lambda cost : cost[PRICE_INDEX] , shopping_list))

# 30% off
# cost_list = list(map(lambda cost : cost[PRICE_INDEX * .7] , shopping_list))

# use reduce to sum up the total
sum = functools.reduce(lambda total, current : total + current, cost_list)
print(sum)

