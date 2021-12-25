
# Task
print("------Caching------")
inp = int(input("Enter the number of values you want to cache:"))
import time
from functools import lru_cache
@lru_cache(maxsize=inp)
def stream(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Start the video and watch to the end")
    stream(5)
    stream(10)
    print("Start the video again from the beginning")
    stream(5)
    stream(5)
    print("Start the video from the mid")


