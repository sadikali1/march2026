# Beginner tutorial for Python sets

# 1. What is a set?
# A set is an unordered collection of unique items.
# Sets automatically remove duplicate values.

# Create an empty set (note: {} creates a dictionary, so use set())

empty_set = set()
print('empty_set:', empty_set)

# Create a set with values
a = {1, 2, 3, 3, 4}
print('set a (duplicates removed):', a)

# Create a set from a list
fruits = set(['apple', 'banana', 'apple', 'orange'])
print('fruits set:', fruits)

# 2. Accessing set items
# Sets are unordered, so we cannot use indexing like lists.
print('\nIterating through a set:')
for item in fruits:
    print(item)

# 3. Adding items to a set
fruits.add('grape')
print('\nAfter add("grape"):', fruits)

# Add multiple items using update()
fruits.update(['kiwi', 'melon', 'banana'])
print('After update([...]):', fruits)

# 4. Removing items from a set
fruits.remove('apple')
print('\nAfter remove("apple"):', fruits)

# discard() does not raise an error if the item is missing
fruits.discard('pear')
print('After discard("pear"):', fruits)

# pop() removes and returns an arbitrary item
removed_item = fruits.pop()
print('popped item:', removed_item)
print('Set after pop():', fruits)

# 5. Checking membership
print('\nIs "banana" in fruits?', 'banana' in fruits)
print('Is "apple" in fruits?', 'apple' in fruits)

# 6. Set operations: union, intersection, difference, symmetric_difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}


# 7. Useful set functions
print('\nlen(set1):', len(set1))
print('min(set1):', min(set1))
print('max(set1):', max(set1))
print('sorted(set1):', sorted(set1))

# 8. Converting between sets and other types
list_from_set = list(set1)
tuple_from_set = tuple(set1)
print('\nlist_from_set:', list_from_set)
print('tuple_from_set:', tuple_from_set)

# 9. Practical example: remove duplicates from a list
numbers = [1, 2, 1, 3, 4, 2, 5]
unique_numbers = list(set(numbers))
print('\noriginal list:', numbers)
print('unique numbers:', unique_numbers)

# 10. Clear a set
set1.clear()
print('\nAfter set1.clear():', set1)
