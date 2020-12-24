# Comparison Operators
# Symbol Use Case 	Bool 	Operation
# 5 < 3 	False 	Less Than
# 5 > 3 	True 	Greater Than
# 3 <= 3 	True 	Less Than or Equal To
# 3 >= 5 	False 	Greater Than or Equal To
# 3 == 5 	False 	Equal To
# 3 != 5 	True 	Not Equal To
#
# And there are three logical operators you need to be familiar with:
# Logical Use 	Bool 	Operation
# 5 < 3 and 5 == 5 	False 	and - Evaluates if all provided statements are True
# 5 < 3 or 5 == 5 	True 	or - Evaluates if at least one of many statements is True
# not 5 < 3 	True 	not - Flips the Bool Value
#
# Here is more information on how George Boole changed the world!



sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
print(san_francisco_pop_density>rio_de_janeiro_pop_density)