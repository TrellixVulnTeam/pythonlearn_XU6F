my_dictionary={"sujay":1,"chandra":2,"delhi":3,"amaravati":4,"hyd":5}
print(my_dictionary)
print(my_dictionary["sujay"])
print(my_dictionary["hyd"])
my_dictionary["hyd"]=7
print(my_dictionary)

print("hyd" in my_dictionary)
print(my_dictionary.get("hyd"))
print(my_dictionary.get("sujay"))

n=my_dictionary.get("dilithum")
print(n is None)
print(n is not None)


population={"shanghai":17.8,"Istanbul":13.3,"Karachi":13.0,"Mumbai":12.5}
print("\n".join(population))

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)


a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a==b)
print(a is b)
print(a==c)
print(a is not c)

# practice
my_prac_dictionary={"sujay":10000,"ram":20300,"hshd":1020}
print(my_prac_dictionary["sujay"])
print("hshs" in my_prac_dictionary)
print("hshd" not in my_prac_dictionary)