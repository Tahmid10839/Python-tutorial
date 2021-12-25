
size = int(input("Enter the size of the list:"))
li = []
for i in range(size):
    li.append(int(input("Enter the list element:")))

r1 = li[:]
r1.reverse()
print(f"The First reveresed list is {r1}")
r2 = li[::-1]
print(f"The Second reversed list is {r2}")
r3 = li[:]
for i in range(len(r3)//2):
    r3[i],r3[len(r3)-i-1] =r3[len(r3)-i-1],r3[i]

print(f"The Third reversed list is {r3}")
if r1==r2==r3:
    print("All three methods have the same reversed list")
