lists=[4,3,6,8,2]
print(len(lists))
print(max(lists))
print(min(lists))
print(sorted(lists))
print(sorted(lists,reverse=True))


newline="\n".join(["sujay","chandra","is","king"])
print(newline)
print("-".join(["sujay","chandra","is","king"]))

appenslist=[1,2,3,4,5]
appenslist.append(6)
appenslist.append(7)
print(appenslist)

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))


names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))


# practice
my_prac_list=[6,7,8,2,3,4,5]
print(max(my_prac_list))
print(min(my_prac_list))
print(len(my_prac_list))
print(sorted(my_prac_list))
print(sorted(my_prac_list,reverse=True))
my_prac_list.append(5555)
print(my_prac_list)
my_name_list=["sujay","chandra","is","super"]
print("-".join(my_name_list))
print("\n".join(my_name_list))