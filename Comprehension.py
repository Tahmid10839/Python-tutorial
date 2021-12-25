
#List
print("List Comprehension:")
ls = [i for i in range(100) if i%2==0]
print(ls)

#Dictionary
print("Dictionary Comprehension:")
dict1 = {i:f"item{i}" for i in range(1,11)}
print(dict1)
dict2 = {value:key for key,value in dict1.items()}
print(dict2)

#Set
print("Set Comprehension:")
fruit = {fr for fr in ["Mango","Apple","Mango","Apple"]}
print(fruit)

#Generators
print("Generator Comprehension:")
gen = (i for i in range(10) if i%2==0)
print(type(gen))
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

#Exercise
no_of_list = int(input("How many items you want to add in the list:"))

item = input("Enter items:")
lis = item.split()
t = int(input("Which comprehension you want to use: 1.List 2.Dictionary 3.Set"))
if t==1:
    ls = [i for i in lis]
    print(ls)
    print(type(ls))

elif t==2:
    dict1 = {i:f"item{i}" for i in lis}
    print(dict1)
    print(type(dict1))
else:
    se = {i for i in lis}
    print(se)
    print(type(se))
