
deck=[2,3,4,5,6,8,10]
hand=[]

while sum(hand) < 17:
    hand.append(deck.pop())

print(hand)

# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while number >= 1:
    product = product * number
    number = number-1

# multiply the product so far by the current number

# increment current with each iteration until it reaches number


# print the factorial of number
print(product)



# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# write your for loop here
for i in range(1,7):
    product = product*i
    number = number-1


# print the factorial of number
print(product)



# number we'll find the factorial of
number = 6
# start with our product equal to one
product = 1

# calculate factorial of number with a for loop
for num in range(2, number + 1):
    product *= num

# print the factorial of number
print(product)




# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1

while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)