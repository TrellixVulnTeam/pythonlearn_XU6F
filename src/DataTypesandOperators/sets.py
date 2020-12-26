names=["sujay","chandra","ram","sita","sita","hanuma"]
print(set(names))

places={"aus","ind","us","uk","jap"}
places.add("braz")
places.add("fra")
print(places)
places.pop()
print(places)


a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()


# practicew
chips=["intel","arm","qualcomm","a14bionic","exygous","arm"]
print(set(chips))

z=[1,2,3,3,4,4,4]
y=set(z)
print(y)
y.add(5)
print(y)
y.pop()
print(y)
