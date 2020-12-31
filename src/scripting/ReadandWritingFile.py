f=open("../data/somefile.txt",'r')
somedata=f.read()
f.close()
print(somedata)

f=open("../data/newfile.txt",'w')
writedata="sujay started the 100 days of coding challenge"
f.write(writedata)
f.close()

f=open("../data/newfile.txt",'a')
write_new_data="and also started to learn tkintter"
f.write(write_new_data)
f.close()

# files = []
# for i in range(10000):
#     files.append(open('../data/some_file.txt', 'r'))
#     print(i)

with open("../data/somefile.txt",'r') as f:
    read_data=f.read()

print(read_data)


with open("../data/camolon.txt",'w') as f:
    data="We're the knights of the round table" \
         "\nWe dance whenever we're able"
    f.write(data)

with open("../data/camolon.txt") as f:
    print(f.read(2))
    print(f.read(8))
    print(f.read())


with open("../data/camolon.txt") as f:
    print(f.readline())

with open("../data/camolon.txt") as f:
    for i in f:
        print(i)



def create_cast_list(filename):
    cast_list = []
    with open("../data/flying_circus_cast.txt",'a') as f:
        for i in range(4):
            name=str(input("enter the cast name"))
            f.write(name+"\n")
            cast_list.append(name)
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    # return cast_list

cast_list = create_cast_list('../data/flying_circus_cast.txt')
with open("../data/flying_circus_cast.txt",'r') as f:
    for actor in f:
        print(actor)
# for actor in cast_list:
#     print(actor)


