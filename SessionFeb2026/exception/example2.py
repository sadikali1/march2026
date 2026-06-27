def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
        return None
    except TypeError:
        print('Error: Please provide numbers for division.')
        return None
    else:
        print('Division successful.')
        return result
    finally:
        print('Finished divide() call.')

if __name__ == '__main__':
    print('Result:', divide(10, 2))
    print()
    print('Result:', divide(10, 0))
    print()
    print('Result:', divide(10, 'a'))
