lst=[]; lst_2=[];
print("List 1 ~ Enter the elements: ")
for i in range(0,5):
	n = input("Enter the element: ")
	lst.append(n)
print("\n", "Enter the elements of the second List[]")
for j in range(0,5):
	n = input("Enter the element: ")
	lst_2.append(n)
print(lst+lst_2)