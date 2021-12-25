
s = set([1,2,3,4,5])
print(type(s))
print(s)

s1 = set()

s1.add(1)
s1.add(2)
s2 = s1.union([3,4,5,2])
print(s1,s2)
s2 = s1.intersection([3,4,5,2])
print(s1,s2)

s3 = set([1,2,3,4])
s4 = set([5,6,7])
print(s3.isdisjoint(s4))

print(len(s3))
s3.remove(3)
print(s3)
print(min(s3))
print(max(s3))
