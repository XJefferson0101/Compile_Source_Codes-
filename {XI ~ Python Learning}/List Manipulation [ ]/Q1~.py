arr = []; new_arr = [] 
lst_range = int(input('Enter the range of a list: '))
for i in range(0,lst_range):
	n = int(input('Enter an integer: '))
	arr.append(n)
count=1 
while lst_range>0:
	lst_range-=count
	new_arr.append(arr[lst_range])
print('Given array: ',arr)
print('Array after reversing: ',new_arr)