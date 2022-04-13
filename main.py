import time

dict = {}

start = time.time()
count = 1
dict['test'] = [start, count]

time.sleep(5)

print(time.time() - dict['test'][0])