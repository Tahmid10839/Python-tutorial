
f1 = open("Tahmid.txt")

try:
    f2 = open("Does2.txt")

except EOFError as e:
    print("This is EOF error",e)
except IOError as e:
    print("This is IO error",e)
else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway.....")
    f1.close()

print("Important Staff")