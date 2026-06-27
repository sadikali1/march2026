def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative.')
    if age < 18:
        raise PermissionError('Must be 18 or older.')
    return 'Access granted.'

if __name__ == '__main__':
    test_ages = [25, 15, -5]

    for age in test_ages:
        try:
            print(f'Checking age {age}:', check_age(age))
        except ValueError as ve:
            print('ValueError:', ve)
        except PermissionError as pe:
            print('PermissionError:', pe)
        finally:
            print('Finished checking', age)
            print()
