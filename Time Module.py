
import time

initial = time.time()
print(initial)
k=0
while(k<10):
    print("This is Tahmid")
    time.sleep(1)
    k+=1
print(f"While loop ran in {time.time()-initial} seconds")

initial2 = time.time()
for i in range(10):
    print("This is Tahmid")

print(f"For Loop ran in {time.time()-initial2} seconds")

local = time.asctime(time.localtime(time.time()))
print(local)