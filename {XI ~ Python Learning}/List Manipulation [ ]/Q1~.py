lst = []; new_lst = []
lst_range = int(input("Enter the range of a List[]: "))
for i in range(0,lst_range):
	n = int(input("Enter an Integer: "))
	lst.append(n)
lst_len = len(lst)
for j in range(0,lst_len):
	var = lst_len-j 
	new_lst.append(var)
print("\n","Original List[]: ",lst)
print(" List[] After reversing: ",new_lst)