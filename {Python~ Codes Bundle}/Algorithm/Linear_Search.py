lst=[1,2,3,4,5]
lst_len=len(lst)
k=0;j=0
n=int(input(": "))
for i in range(0,lst_len):
	if lst[i]==n: 
		k=1 
	else:
		j=1
if k==1:
	print('Yes')
else:
	print("No")