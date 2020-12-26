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
