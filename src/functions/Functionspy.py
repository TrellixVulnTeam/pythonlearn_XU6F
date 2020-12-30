def Volumeofcyclinder(radius,height):
    pi=3.14159
    return height*pi*radius**2

print(Volumeofcyclinder(10,2))



# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)

# this returns something
def add_ten(num):
    return(num + 10)

print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_1))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))


def mydefaultvalue(height,radius=4):
    return radius

print(mydefaultvalue(10))



# write your function here
def population_density(population,landarea):
    return population/landarea



# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))


def readable_timedelta(days):
    years=days%365
    month=days%30
    week=days%7

    if years>0:
        print("years = {}".format(years))
    if month>0:
        print("months: {}".format(month))
    if week>0:
        print("week: {}".format(week))
    if days<6:
        print("days: {}".format(days))

readable_timedelta(366)


def readable_timedeltas(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedeltas(10))


egg_count = 0

def buy_eggs(varible):
   varible += 12 # purchase a dozen eggs
   return varible

egg_count=buy_eggs(egg_count)