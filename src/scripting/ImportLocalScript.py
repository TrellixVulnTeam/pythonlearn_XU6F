from src.scripting import UsefulFunctions as uf
import math
import random

print(uf.sum(10,20))
print(uf.sub(20,10))
print(uf.mul(10,20))
print(uf.div(10,20))

print(math.e**3)





# Use an import statement at the top

word_file = "words.txt"
word_list = []

#fill up the word_list
with open("../data/words.txt",'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces
# def generate_password():
#     password =""
#     for i in range(3):
#      num=random.randint(0, len(word_list))
#      password += word_list[num]
#     return password


def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)


# test your function
print(generate_password())