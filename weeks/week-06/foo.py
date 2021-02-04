def say_hello(name):
    return 'Hello, {}!'.format(name)


class Person:
    """
    Docstring for this class.
    """
    kind = 'homosaphien'
    
    def __init__(self, name) -> None:
        self.name = name


# this is an `if` statement, because we don't want the next lines
# to run, unless this module is called from a command line 
# application.
if __name__ == '__main__':
    """
    Entry point of this python file.
    """
    print('Foo module ran successfully.')

# uncomment these lines if you want to see how if/ else works 
# on imports
# else:
#     print('not run from command line')