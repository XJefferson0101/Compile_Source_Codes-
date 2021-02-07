class Linear_Search():
	try:
		k=0;k1=0
		def L_Search():
			lst=[] 
			lst_sort=[] 
			lst_range=int(input("Enter the range of the list[]: "))
			for i in range(lst_range):
			    lst_n=int(input("Integer elemets: "))
			    lst.append(lst_n)
			lst_sort=sorted(lst)
			lst_len=len(lst) 
			for j in range(0,lst_len):
			    if lst[j]==lst_n:
			    	k=1
			     else:
			    	k1=1
			 if k==1:
			 	print("list[] after sorted: ",lst_sort)
			 	print("The Enter number is on the list[]")
			 else:
			 	print("Not on the list[]")
	except Exception as e: 
		print(e)
Linear_Search.L_Search()