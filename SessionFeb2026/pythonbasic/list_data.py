my_list12 = []
print("Empty list:", my_list12)

my_list = [10, 2, 12, 4, 8, 6]
print("Original list:", my_list)
my_list.sort()
print("Sorted list:", my_list)

my_list.sort(reverse=True)
print("Sorted list (descending):", my_list)

my_list1 = [1, 2, 3, 4, 5, 100.5, "Hello", 1, 2, True, False]
print("Modified list:", my_list1)

my_list1.append("World")
print("List after appending 'World':", my_list1)

my_list1.insert(2, "Inserted")
print("List after inserting 'Inserted' at index 2:", my_list1)

#my_list1.extend([6, 7, 8])
#print("List after extending with [6, 7, 8]:", my_list1)

my_list1[1] = "Updated"
print("List after updating index 1 with 'Updated':", my_list1)


my_list1.remove("Hello")
print("List after removing the first occurrence of 'Hello':", my_list1)

del my_list1[3]
print("List after deleting the element at index 3:", my_list1)

for item in my_list1:
    print("List item:", item)

print("Length of the list:", len(my_list1))

print("Minimum value in the list:",   my_list1[3])