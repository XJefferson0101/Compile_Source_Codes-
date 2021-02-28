lst = []; count = 1; new_lst = [] 
lst_range = int(input(" Enter the range of a List[]: "))
for i in range(0,lst_range):
	n = int(input(" Enter an Integer: ")) 
	lst.append(n)
lst_len = len(lst)
for j in range(0,lst_len):
	count+=j
	get_var = lst[lst_len-count]
	new_lst.append(get_var)
print(' Given List[]: ',lst)
print('List[] after reversing: ',new_lst)