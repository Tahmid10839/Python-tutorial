
f = open("Tahmid.txt","w")
f.write("Tahmid is a good boy\n")
f.close()

f = open("Tahmid.txt","a")
f.write("Tahmid study in CSE\n")
f.close()

f = open("Tahmid.txt","a")
a = f.write("Tahmid study in DIU\n")
print(a)
f.close()
