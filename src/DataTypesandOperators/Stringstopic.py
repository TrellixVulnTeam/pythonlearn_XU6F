first_word="hello"
second_word='world'

print(first_word+' '+second_word)

print(first_word*5)

print(len(second_word))

sentence="this the way \' you can add the single quotation"
print(sentence)
print(len(sentence))
print(sentence[0])


# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print(ford_quote)



username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20
print(username+" accessed the site "+url+" at "+timestamp)


given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name)+len(middle_names)+len(family_name)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

# print(len(835))