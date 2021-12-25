
# rb = read binary
# rt = read text - default

f = open("Tahmid.txt","r")
print(f.read())
f.close()

f = open("Tahmid.txt","r")
print(f.read(3))
print(f.read(3))
f.close()

f = open("Tahmid.txt","r")
#for line in f:
#    print(line,end="")

print(f.readline())
print(f.readline())
f.close()

f = open("Tahmid.txt","r")
print(f.readlines())
f.close()