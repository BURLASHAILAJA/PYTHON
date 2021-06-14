'''

Welcome to GDB Online.
'''
n = int(input("Enter number of elements:")) 
# Below line read inputs from user using map() function 
#Taking inputs horital fasion in list.
a = list(map(int,input().split()))[:n] 
a.sort()
p=a[0]+a[1]
s=a[4]
re=s-p
print(re)
