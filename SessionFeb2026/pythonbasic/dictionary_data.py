# Beginner tutorial for Python dictionaries

# 1. What is a dictionary?
# A dictionary stores key-value pairs. Keys are unique and can be used to look up values.

# Create a dictionary
blank_dict = {}
print('blank_dict:', blank_dict)

person = {'name': 'Alice', 'age': 28, 'city': 'New York'}
print('person:', person)

# Access dictionary values by key
print('\nName:', person['name'])
print('Age:', person['age'])

# Use get() to avoid KeyError
print('Country:', person.get('country', 'Not specified'))

# 2. Add or update items
# Assigning to a key adds it if it does not exist, or updates it if it does.
person['country'] = 'USA'   # adds a new key
person['age'] = 29         # updates the existing value for 'age'
print('\nAfter add/update:', person)

# 3. Remove items
removed_age = person.pop('age')
print('\nRemoved age:', removed_age)
print('After pop:', person)

# popitem() removes the last inserted item (Python 3.7+ preserves insertion order)
last_item = person.popitem()
print('Popped item:', last_item)
print('After popitem:', person)

# 4. Keys, values, and items
person = {'name': 'Alice', 'age': 28, 'city': 'New York'}
print('\nKeys:', person.keys())
print('Values:', person.values())
print('Items:', person.items())

# 5. Iterate through dictionary
print('\nIterate keys:')
for key in person:
    print(key, '->', person[key])

print('\nIterate items:')
for key, value in person.items():
    print(key, '->', value)

# 6. Dictionary methods
person.update({'age': 28, 'country': 'USA'})
print('\nAfter update():', person)

print('Contains name?', 'name' in person)
print('Contains salary?', 'salary' in person)

# 7. Copying dictionaries
person_copy = person.copy()
person_copy['name'] = 'Bob'
print('\nOriginal:', person)
print('Copy:', person_copy)

# 8. Nested dictionaries
students = {
    'student1': {'name': 'John', 'grade': 'A'},
    'student2': {'name': 'Emma', 'grade': 'B'}
}
print('\nNested dictionary:', students)
print('student1 name:', students['student1']['name'])

# 9. Practical example: counting items
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
print('\nWord counts:', count)

# 10. Clear a dictionary
count.clear()
print('After clear():', count)


# class example
# objeccts
# OOPS concetps 
# Class, Object, Inheritance, Polymorphism, Encapsulation, Abstraction

# Abstraction
# Access modifiers
# Exceptions handling

# Playwright 
