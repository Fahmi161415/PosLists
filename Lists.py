# Program to print positive numbers in a list

list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
print("Original numbers in the list : ", list1)
new_list1 = list(filter(lambda x:x>0,list1))
print("Psitive numbers in the list : ",new_list1)

print("Original numbers in the list : ", list2)
new_list2 = list(filter(lambda x:x>0,list2))
print("Positive numbers in the list : ",new_list2)





     
     
