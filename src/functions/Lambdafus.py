def multiply(x, y):
    return x * y

multiplys= lambda x,y:x*y
print(multiplys(10,20))



numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

# def mean(num_list):
#     return sum(num_list) / len(num_list)

averages = list(map(lambda num_list: sum(num_list) / len(num_list), numbers))
print(averages)



cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

# def is_short(name):
#     return len(name) < 10

short_cities = list(filter(lambda name: len(name) < 10, cities))
print(short_cities)