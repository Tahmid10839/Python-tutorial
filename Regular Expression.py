import re

# findall, search, split, sub, finditer

str = '''Tahmid isis a bad boy.
He study in CSE.
He read in DIU +8801515637957'''

p = re.compile(r"[+][8][8]\d{11}")
l = []
mat = p.finditer(str)
for m in mat:
    print(m)
    l.append(m)

print(l)
