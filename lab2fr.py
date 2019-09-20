import random, time
data = list(range(2500))
random.shuffle(data)
def insertionSort(arr):  
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
start_time = time.time()
insertionSort(data)
elapsed_time = time.time() - start_time
print (data) 
print(elapsed_time)
