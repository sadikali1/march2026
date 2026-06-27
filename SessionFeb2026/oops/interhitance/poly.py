class PolyExample:
    def area(self, length, width=None):
        """Demonstrates method overloading-like behavior in Python.
        If only length is provided, calculate square area.
        If both length and width are provided, calculate rectangle area.
        """
        if width is None:
            return length * length
        return length * width

if __name__ == '__main__':
    poly = PolyExample()

    print('Square area (4):', poly.area(4))
    print('Rectangle area (4x5):', poly.area(4, 5))
