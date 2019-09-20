data = input("Enter anything. It'll sort. ")
data  = data.split()
import re 
def sorted_nicely( l ): 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)
for x in sorted_nicely(data):
    print(x)