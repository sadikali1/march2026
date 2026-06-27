# Tuple examples and common tuple operations in Python

# 1. Tuple creation
empty_tuple = ()
single_item = (42,)
single_item1 = 42,43,45  # This is not a tuple, it's just an integer
mixed_tuple = (1, 'apple', 3.14, True)
nested_tuple = (1, (2, 3), [4, 5])
print('empty_tuple:', empty_tuple)
print('single_item:', single_item)
print('single_item1:', single_item1)
print('mixed_tuple:', mixed_tuple)
print('nested_tuple:', nested_tuple)

# 2. Tuple constructor
from_list = tuple([10, 20, 30])
from_string = tuple('hello')
print('\nfrom_list:', from_list)
print('from_string:', from_string)

# 3. Accessing tuple items
print('\nfirst item of mixed_tuple:', mixed_tuple[0])
print('last item of mixed_tuple:', mixed_tuple[-1])
print('slice mixed_tuple[1:3]:', mixed_tuple[1:3])

# 4. Tuple immutability
try:
    mixed_tuple[1] = 'banana'
except TypeError as err:
    print('\nTuple immutability:', err)

# 5. Concatenation and repetition
tuple_a = (1, 2, 3)
tuple_b = ('a', 'b')
concat = tuple_a + tuple_b
repeat = tuple_b * 3
print('\nconcat:', concat)
print('repeat:', repeat)

# 6. Membership test
print('\nIs 2 in tuple_a?', 2 in tuple_a)
print('Is "x" not in tuple_b?', 'x' not in tuple_b)

# 7. Length, min, max, sum
print('\nlen(tuple_a):', len(tuple_a))
print('min(tuple_a):', min(tuple_a))
print('max(tuple_a):', max(tuple_a))
print('sum(tuple_a):', sum(tuple_a))

# 8. count() and index()
numbers = (1, 2, 2, 3, 2, 4)
print('\nnumbers.count(2):', numbers.count(2))
print('numbers.index(3):', numbers.index(3))

# 9. Sorted tuple values -> returns list
sorted_numbers = sorted(numbers)
print('\nsorted(numbers):', sorted_numbers)

# 10. Unpacking tuples
person = ('Alice', 28, 'Engineer')
name, age, profession = person
print('\nUnpacked values:')
print('name =', name)
print('age =', age)
print('profession =', profession)

