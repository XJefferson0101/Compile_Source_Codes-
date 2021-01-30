lst=[]
for lst_l in range(5):
	lst_n = int(input(": "))
	lst.append(lst_n)
lst_len=len(lst)
k=0;j=0
n=int(input("Enter num to be search: "))
for i in range(0,lst_len):
	if lst[i]==n: 
		k=1 
	else:
		j=1
if k==1:
	print('Yes')
else:
	print("No")