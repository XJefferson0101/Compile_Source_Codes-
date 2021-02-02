lst=[]  # Create an empty list[] 
for lst_l in range(5):  # range of the list[]
	lst_n = int(input(": "))  # Elements to be put to the the list[]
	lst.append(lst_n)  
lst_len=len(lst)  # legth of the list[]
k=0;j=0
n=int(input("Enter num to be search: "))
for i in range(0,lst_len):
	if lst[i]==n: 
		k=1 
	else:
		j=1
if k==1:
	print('The Enter number is on the list[]')  #</>
else:
	print("No")