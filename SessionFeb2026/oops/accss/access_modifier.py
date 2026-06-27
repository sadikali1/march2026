class AccessModifierExample:

    def __init__(self, a1, a2, a3):
        self.public_value = a1
        self._protected_value = a2
        self.__private_value = a3

    def show_values(self):
        print('Public:', self.public_value)
        print('Protected:', self._protected_value)
        print('Private:', self.__private_value)

    def get_private_value(self):
        return self.__private_value

    def set_private_value(self, value):
        self.__private_value = value

class DerivedExample(AccessModifierExample):
    def access_values(self):
        print('Derived public:', self.public_value)
        print('Derived protected:', self._protected_value)
       # print('Private:', self.__private_value)
        # private attribute is name-mangled and not directly inherited
      

if __name__ == '__main__':
    example = AccessModifierExample('A11', 'A22', 'A33')
    example.show_values()

    print('\nAccess from outside:')
    print('Public direct:', example.public_value)
    print('Protected direct (convention):', example._protected_value)
    #print('Private direct:', example.__private_value)

    print('\nAccess via getter:', example.get_private_value())
    example.set_private_value('A11')
    print('Private after setter:', example.get_private_value())

    print('\nDerived class access:')
    derived = DerivedExample('public data', 'protected data', 'private data')
    derived.access_values()



