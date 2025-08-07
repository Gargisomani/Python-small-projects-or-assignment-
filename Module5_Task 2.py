list1=[1,2,3,4,5,6,7,8,9,10]
print("Original list:",list1)
list2=list1[0:5]
print("Extracted first five elements:",list2)
print("Extracted last five elements:",list(list2.__reversed__()))



