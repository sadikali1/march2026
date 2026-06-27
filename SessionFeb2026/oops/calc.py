# Beginner Calc class with instance and static method tutorials

class Calc:
    """A calculator with both instance methods (operate on internal state)
    and static methods (operate on provided arguments).

    Instance methods update `self.last_result` and return it. Static
    methods are simple pure functions that do not depend on instance state.
    """

    def __init__(self, start_value: float = 0.0):
        # store the last computed value for chained operations
        self.last_result = float(start_value)

    # Instance methods (operate on self.last_result)
    def add(self, x: float):
        self.last_result += x #  self.last_result = self.last_result + x
        return self.last_result

    def subtract(self, x: float):
        self.last_result -= x
        return self.last_result

    def multiply(self, x: float):
        self.last_result *= x
        return self.last_result

    def divide(self, x: float):
        if x == 0:
            raise ValueError('Cannot divide by zero')
        self.last_result /= x
        return self.last_result

    def clear(self):
        """Reset the calculator's state to zero."""
        self.last_result = 0.0
        return self.last_result

    def get_last(self):
        return self.last_result

    # Static methods (pure functions)
    @staticmethod
    def stat_add(a, b):
        return a + b

    @staticmethod
    def stat_subtract(a, b):
        return a - b

    @staticmethod
    def stat_multiply(a, b):
        return a * b

    @staticmethod
    def stat_divide(a, b):
        if b == 0:
            raise ValueError('Cannot divide by zero')
        return a / b


if __name__ == '__main__':
    # Tutorial: using instance methods (maintain internal state)
    calc = Calc(10)  # start with 10
    print('Starting value:', calc.get_last())
    print('add(5) ->', calc.add(5))          # 15
    print('multiply(2) ->', calc.multiply(2))# 30
    print('subtract(4) ->', calc.subtract(4))# 26
    try:
        print('divide(0) ->', calc.divide(0))
    except ValueError as e:
        print('Instance divide error:', e)
    print('divide(2) ->', calc.divide(2))    # 13.0
    print('clear() ->', calc.clear())        # 0.0

    # Tutorial: using static methods (no internal state)
    print('\nStatic method usage:')
    print('stat_add(3,5) =', Calc.stat_add(3, 5))
    print('stat_subtract(10,4) =', Calc.stat_subtract(10, 4))
    print('stat_multiply(6,7) =', Calc.stat_multiply(6, 7))
    print('stat_divide(20,4) =', Calc.stat_divide(20, 4))
