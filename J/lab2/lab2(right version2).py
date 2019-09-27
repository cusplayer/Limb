import random, time
data = list(range(2500))
random.shuffle(data)
def insertionSort(alist):
   for i in range(len(data)):  
    min_idx = i 
    for j in range(i+1, len(data)): 
        if data[min_idx] > data[j]: 
            min_idx = j          
    data[i], data[min_idx] = data[min_idx], data[i]   
start_time = time.time()
insertionSort(data)
elapsed_time = time.time() - start_time
print (data) 
print(elapsed_time)
