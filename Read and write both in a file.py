
# Handle read and write both

f = open("Tahmid.txt","r+")
print(f.read())
f.write("Thank You")

f.close()