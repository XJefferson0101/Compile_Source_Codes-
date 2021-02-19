#</>
class List_func():
	try:
		def input_List():
			lst = []
			for i in range(5):
				n = int(input("Input any integer val: "))
				lst.append(n)
			print("                 ")
			print("Input List: ", lst)
		
		def concat_List():
			lst1 = [1,2,3,4,5]
			lst2 = [6,7,8,9,10]
			print(lst1+lst2)

		def Sort_List():
			lst_Sort = [34,45,1,56,2,1,3,100000000,3,76,1,12,123,5,4,34,3,45]
			print("Given List:  ",lst_Sort)
			print("Sorted List[]: ",sorted(lst_Sort))

	except Exception as e:
		print(e)

List_func.input_List()
List_func.concat_List()
List_func.lst_Sort()