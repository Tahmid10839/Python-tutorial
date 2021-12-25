
gen = (i for i in range(1,11) if i%2==0)
print(type(gen))
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
