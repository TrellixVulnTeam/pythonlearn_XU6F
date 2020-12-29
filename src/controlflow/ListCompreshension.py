citys=["Amaravati","Hyd","Vizag","Jalandhar","chennai","Banglore"]
comprhension_city=[city.title() for city in citys]
print(comprhension_city)

xx=[1,2,3,4,5]
squares=[x**2 for x in xx if x%2==0]
print(squares)
squares=[x**2 if x%2==0 else x+2  for x in xx]
print(squares)



names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [na.lower() for na in names]
print(first_names)

multiples_3 = [x for x in range(1,21) if x%3==0]
print(multiples_3)


scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [va   for va,na in scores.items() if na >= 65]

print(passed)