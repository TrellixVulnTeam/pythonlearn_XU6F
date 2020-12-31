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