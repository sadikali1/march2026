"""Demonstrate different method parameter types in a class.

Examples included:
- positional parameters
- default values
- keyword-only parameters
- variable positional parameters (`*args`)
- variable keyword parameters (`**kwargs`)
- mutable default value pitfall and safe alternative
"""


class MethodsExample:
    def positional(self, a, b):
        """Simple positional parameters."""
        return f'positional: a={a}, b={b}'

    def defaults(self, a, b=10, c='x'):
        """Parameters with default values (b and c)."""
        return f'defaults: a={a}, b={b}, c={c}'

    def varargs(self, *args):
        """Variable positional arguments collected into a tuple."""
        return f'varargs: args={args}'

    def varkw(self, **kwargs):
        """Variable keyword arguments collected into a dict."""
        return f'varkw: kwargs={kwargs}'


if __name__ == '__main__':
    m = MethodsExample()

    print(m.positional(1, 2))
    print(m.defaults(5))
    print(m.defaults(5, c='z'))
    print(m.defaults(5, b=20, c='z'))
    print(m.varargs(1, 2, 3, 'a'))
    print(m.varkw(alpha=1, beta=2))

 