lst=[]; chk=0 
lst_range =int(input('Enter tha range of data: '))
search_n = input('Enter the element to be search: ')
for i in range(0,lst_range):
	ele = input(' Enter the element: ')
	lst.append(ele)
	if(search_n==ele):
		chk+=1
if(chk!=0):
	print(' Given elements: ',lst)
	print(search_n,' Is found at position ',lst.index(search_n))
else:
	print(' Given elements: ',lst)
	print(search_n,"Is not found!!!!!!!!")