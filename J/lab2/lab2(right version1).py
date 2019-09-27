import random, time
data = list(range(2500))
random.shuffle(data)
def insertionSort(alist):
   for i in range(1,len(alist)):
       current = alist[i]
       while i>0 and alist[i-1]>current:
           alist[i] = alist[i-1]
           i = i-1
           alist[i] = current   
start_time = time.time()
insertionSort(data)
elapsed_time = time.time() - start_time
print (data) 
print(elapsed_time)
