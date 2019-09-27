import random, time
data = list(range(2500))
random.shuffle(data)
start_time = time.time()
print(sorted(data))
elapsed_time = time.time() - start_time
print(elapsed_time)
