lst=[5,4,3,2,1]
new_lst=[]
lst_len = len(lst)
for i in range(0,lst_len):  # Nested for loop{}
    for j in range(1,lst_len):
    	if lst[i] == lst[j]:
    		new_lst.append(lst[j])
print(new_lst)


