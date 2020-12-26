list=[23,1.34,"sujay",True]

print(list[0])
print(list[-1])
print(len(list))

print(list[:2])
print(list[1:3])
print(list[1:])

print(23 in list)
print(23 not in list)
print("sujay" in list)
print(True in list)
print(True not in list)


# lists are ordered and mutable
list[0]="one"
print(list)

# string are ordered and immutable
name="sujay"
# name[0]="A"




month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
num_days=days_in_month[month]

print(num_days)

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])