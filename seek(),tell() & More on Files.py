
f = open("Tahmid.txt")

print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())

f.close()

f = open("Tahmid.txt")
print(f.readline())
f.seek(0)
print(f.readline())
f.close()