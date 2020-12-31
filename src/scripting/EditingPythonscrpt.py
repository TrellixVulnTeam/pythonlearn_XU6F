num_of_snakes = 1
snakes= """"
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""

print(snakes*num_of_snakes)

names =  input("enter the names seperted by a comma").title().split(",")
assignments =  input("enter the assignments seperated by a comma").split(",")
grades =  input("enter the grades seperated by comma").split(",")

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name,asss,gra in zip(names,assignments,grades):
    print(message.format(name,asss,gra,int(gra)+int(asss)*2))