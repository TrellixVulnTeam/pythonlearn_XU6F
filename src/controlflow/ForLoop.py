cities=["amaravati","hyderabad","chennai","banglore","mumbai","Kolkata","vizag"]
for city in cities:
    print(city)

for city in range(len(cities)):
    cities[city]=cities[city].title()
    print(cities[city])

for i in range(0,10,2):
    print(i)


sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
for i in sentence:
    print(i)

for i in range(5,31,5):
    print(i)

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for i in range(len(names)):
    names[i]=names[i].lower()
    names[i]=names[i].replace(" ","_")
    usernames=names



print(usernames)


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)



tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for i in range(len(tokens)):
    if(tokens[i].startswith("<")):
        count=count+1


print(count)

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for str in items:
    html_str+= "<li>"+str+"</li>\n"

html_str += "<ul>"


print(html_str)