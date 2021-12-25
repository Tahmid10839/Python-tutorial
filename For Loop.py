list1=[["Tahmid",1],["Rahim",2],["Karim",3]]

for item,lollypop in list1:
    print(item,lollypop)

dict1 = dict(list1)

for item,lollypop in dict1.items():
    print(item,lollypop)

for item in dict1:
    print(item)

for item,lollypop in dict1.items():
    if lollypop > 1:
        print(item,lollypop)

list2 = ['Tahmid','Rahim',int,5,3,2,10,20,60,70]

for item in list2:
    if str(item).isnumeric() and item>6:
        print(item)

num1 = int(input("Enter a number:"))
print("Multiplication:")
for i in range(1,11):
    print(num1,'*',i,'=',num1*i)