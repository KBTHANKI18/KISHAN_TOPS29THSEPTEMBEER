# Differentiate between append () and extend () methods? 
#append() method adds a single element to the end of the list, while extend() method adds multiple elements to the end of the list.
#append() method modifies the original list by adding the new element as a single item, while extend() method modifies the original list by adding each element of the iterable as individual items to the end of the list.
l1= [1, 2, 3]
l2 = [4, 5, 6]
l1.append(l2)
print(l1)  
l1.extend(l2)
print(l1)  
