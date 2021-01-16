# Week 5 - Operators, Execution Model, Expressions 

- [Week 5 - Operators, Execution Model, Expressions](#week-5---operators-execution-model-expressions)
  - [Operators](#operators)
    - [Arithmetic Operators (+, -, *, /, //, %, **)](#arithmetic-operators--------)
    - [Bitwise Operators (&, |, ^, >>, <<, ~)](#bitwise-operators------)
    - [Assignment Operators (=, +=, -=, /=, //= etc.)](#assignment-operators-------etc)
    - [Comparison Operator (==, !=, >, <, >=, <=)](#comparison-operator------)
    - [Logical Operators (and, or, not)](#logical-operators-and-or-not)
    - [Identity Operators (is, is not)](#identity-operators-is-is-not)
    - [Membership Operators (in, not in)](#membership-operators-in-not-in)
  - [Execution Model](#execution-model)
    - [Control Flow](#control-flow)
      - [The if statement](#the-if-statement)
      - [The while statement](#the-while-statement)
      - [The for statement](#the-for-statement)
      - [The try statement](#the-try-statement)
      - [The with statement](#the-with-statement)
    - [Simple Statements](#simple-statements)
      - [The assert statement](#the-assert-statement)
      - [The pass statement](#the-pass-statement)
      - [The del statement](#the-del-statement)
      - [The return statement](#the-return-statement)
      - [The yield statement](#the-yield-statement)
      - [The raise statement](#the-raise-statement)
      - [The break statement](#the-break-statement)
      - [The continue statement](#the-continue-statement)
      - [The import statement](#the-import-statement)
      - [The global statement](#the-global-statement)
      - [The nonlocal statement](#the-nonlocal-statement)

## Operators

### Arithmetic Operators (+, -, *, /, //, %, **)

All unary arithmetic and bitwise operations have the same priority.

The unary `-` (minus) operator yields the negation of its numeric argument.

``` py
assert 5 - 3 == 2
```

The unary `+` (plus) operator yields its numeric argument unchanged. This operator yields the sum of its arguments.

``` py
# classical numbers
assert 5 + 3 == 8

# concatenating strings can be done 
>>> '2' + '2'
'22'

# sequences can be join together
>>> [2,3,4,5] + [6,7,]
[2, 3, 4, 5, 6, 7]
```

The unary `~` (invert) operator yields the bitwise inversion of its integer argument. The bitwise inversion of `x` is defined as `-(x+1)`. It only applies to integral numbers.

``` py
>>> ~(2 + 1)
-4
```

The `*` (multiplication) operator yields the product of its arguments. The arguments must either 
- both be numbers, 
- one argument must be an integer and the other must be a sequence. 

``` py
# numbers only
>>> 2 * 3
6

# numbers only with decimals
>>> 2 * 3.3
6.3

# with a number and a a tuple (immutable type)
>>> 2 * (3, 4, 5, 6, 7)
(3, 4, 5, 6, 7, 3, 4, 5, 6, 7)

# with a number and a list
>>> 2 * [3, 4, 5, 6, 7]
[3, 4, 5, 6, 7, 3, 4, 5, 6, 7]

# with a list and a list
>>> [2] * [3, 4, 5, 6, 7]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-8e1106c0570e> in <module>
----> 1 [2] * [3, 4, 5, 6, 7]

TypeError: can't multiply sequence by non-int of type 'list'
```

The `/` (division) and `//` (floor division) operators yield the quotient of their arguments. The numeric arguments are first converted to a common type. 

- Division of integers yields a float, while floor division of integers results in an integer; the result is that of mathematical division with the ‘floor’ function applied to the result. 
- Division by zero raises the ZeroDivisionError exception.


``` py
# division
assert 5 / 3 == 1.6666666666666667
assert 8 / 4 == 2
assert isinstance(8 / 4, float)

# floor division
assert 5 // 3 == 1
assert isinstance(5 // 3, int)
```

The `%` (modulo) operator yields the remainder from the division of the first argument by the second. The numeric arguments are first converted to a common type. 

- A zero right argument raises the ZeroDivisionError exception.
- The modulo operator always yields a result with the same sign as its second operand (or zero)

``` py
x = 2
y = 3
assert x == (x//y)*y + (x%y)

# builtin function divmod relates with `//` and `%` following way
divmod(x, y) == (x//y, x%y)

# modulo operator can be used to perform old-style string formatting
>>> 'My name is %s!' % 'Metin'
'My name is Metin!'
```

The `**` (power) operator is used in python in the following way.

``` py
>>> pow(2,3)
8

# with ** syntax
>>> 2 ** 3
8

# power of a negative value
>>> -2 ** 3

# to get the power of -2
>>> (-2)**4
16

# powering to -2
>>> 10**-2
0.01

# cannot raise 0 to a minus power
>>> (0)**-1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: 0.0 cannot be raised to a negative power
```

### Bitwise Operators (&, |, ^, >>, <<, ~)

Bitwise operations only make sense for integers. The result of bitwise operations is calculated as though carried out in two’s complement with an infinite number of sign bits.

Each of the three bitwise operations has a different priority level. This table lists the bitwise operations sorted in ascending priority:

| Operation | Result                          |
| --------- | ------------------------------- |
| x `|` y   | bitwise or of x and y           |
| x ^ y     | bitwise exclusive or of x and y |
| x & y     | bitwise and of x and y          |
| x << n    | x shifted left by n bits        |
| x >> n    | x shifted right by n bits       |
| ~x        | the bits of x inverted          |

``` py
# AND
# Sets each bit to 1 if both bits are 1.
#
# Example:
# 5 = 0b0101
# 3 = 0b0011
assert 5 & 3 == 1  # 0b0001

# OR
# Sets each bit to 1 if one of two bits is 1.
#
# Example:
# 5 = 0b0101
# 3 = 0b0011
assert 5 | 3 == 7  # 0b0111

# XOR
# Sets each bit to 1 if only one of two bits is 1.
#
# Example:
# 5 = 0b0101
# 3 = 0b0011
number = 5  # 0b0101
number ^= 3  # 0b0011
assert 5 ^ 3 == 6  # 0b0110
```

<sub> Some examples are from [learn-python](https://github.com/trekhleb/learn-python/blob/master/src/operators/test_bitwise.py) repository.</sub>  
<sub> More on table notes is in [bitwise-operations-on-integer-types](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types) at python documentation.</sub>

### Assignment Operators (=, +=, -=, /=, //= etc.)

Some assignment operators.

``` py
n = 1
c = 10
z = 100
for i in range(5):
    n += 1
    c -= 2
    z /= 3
```

An `:=` (assignment expression) (sometimes also called a “named expression” or “walrus”) assigns an expression to an identifier, while also returning the value of the expression.

``` py
# set value within if condition
for letter in ('A', 'B', 'C'):
    if value := 'A':
        print(value + letter)
```

### Comparison Operator (==, !=, >, <, >=, <=)

Some notes on comparison operators.

- In Python have the same priority, which is lower than that of any arithmetic, shifting or bitwise operation. 
- Comparisons yield boolean values: True or False.
- Note that `a op1 b op2 c` doesn’t imply any kind of comparison between `a` and `c`, so `x < y > z` is good.
- 
``` py
x, y, z = 2, 5, 1

# can be chained
>>> x < y <= z 
False

# above is equivalent to 
>>> x < y and y <= z
False

# legal!
>>> x < y > z
True
```

The operators <, >, ==, >=, <=, and != compare the values of two objects. The objects do not need to have the same type.

### Logical Operators (and, or, not)

Combine conditional statements using logical operators.

``` py
# Let's work with these number to illustrate logic operators.
a = 5
b = 10

# Returns True if both statements are true.
assert a > 0 and b < 20

# Returns True if one of the statements are true.
assert a > 0 or b < 20

# Reverse the result of of condition
assert not a == b
assert a == b
```

### Identity Operators (is, is not)

The operators is and is not test for an object’s identity: `x is y` is true if and only if x and y are the same object. 

An Object’s identity is determined using the `id()` function. `x is not y` yields the inverse truth value.

``` py
v = False
>>> v is False
True

class A:
    pass

# set another pointer to a
a = A()
b = a
>>> a is b
True

# a new instance for each variable
a = A()
b = A()
>>> a is b
False
```

### Membership Operators (in, not in)

The operators in and not in test for membership. 

- `x in s` evaluates to `True` if x is a member of s, and False otherwise. 
- `x not in s` returns the negation of x in s. 
- All built-in sequences and set types support this as well as dictionary, for which in tests whether the dictionary has a given key. 
- For container types such as list, tuple, set, frozenset, dict, or collections.deque, the expression `x in y` is equivalent to `any(x is e or x == e for e in y)`.

``` py
# dictionaries
stocks = dict(tesla=800.00, apple=135.50)
assert 'tesla' in stocks
assert 'fb' not in stocks

# container types
fruit_list = ["apple", "banana"]
assert "banana" in fruit_list
assert "peach" not in fruit_list
assert any("banana" is e or "banana" == e for e in fruit_list)

```

## Execution Model

### Control Flow

#### The if statement

The statement `if` is to check conditional statements.

``` py
if condition_to_check:
    print('Condition returns', True)
else:
    print('Condition returns', False)
```

There can be zero or more `elif` parts, and the `else` part is optional. The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation.

``` py
# get an input and do some operation
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```

#### The while statement

The while statement is used for repeated execution as long as an expression is true:

``` py
while some_expression_to_check:
    # do some operation
    pass
```

This repeatedly tests the expression and, if it is true, executes the first suite; if the expression is false (which may be the first time it is tested) the suite of the else clause, if present, is executed and the loop terminates.


#### The for statement

The for statement is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable object, in the order that they appear in the sequence:

``` py
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```

Iterating over mutable objects while modifying can have unexpected results.

``` py
users = {
  'Mike': 1,
  'John': 2,
  'Smith': 3,
  'Susanne': 4,
}

# will throw RuntimeError
for key, value in users.items():
    if value == 2:
        del users[key]
        print(key, users)

# get a copy of the dictionary while iterating
for key, value in users.copy().items():
    if value == 2:
        del users[key]
        print(key, users)

# create a new dictionary 
new_users = {}
for key, value in users.items():
    if value == 3:
        continue
    new_users[key] = value
    print(key, users)
```

#### The try statement

The try statement works as follows.

First, the try clause (the statement(s) between the try and except keywords) is executed.

If no exception occurs, the except clause is skipped and execution of the try statement is finished.

If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try statement.

If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements

``` py
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```

A try statement may have more than one except clause, to specify handlers for different exceptions. At most one handler will be executed. Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same try statement. An except clause may name multiple exceptions as a parenthesized tuple, for example:

``` py
try:
    1 is None
except (RuntimeError, TypeError, NameError):
    pass
except SyntaxError:
    print('Yey')
except:
    print('An exception that is not defined in above clauses occured')
```

The `try` statement can also have an optional `else` statement.

``` py
try:
    f = open('some_file.txt', 'r')
except OSError:
    print('cannot open', 'some_file.txt')
else:
    print('some_file.txt', 'has', len(f.readlines()), 'lines')
    f.close()
```

The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try … except statement.

When an exception occurs, it may have an associated value, also known as the exception’s argument. The presence and type of the argument depend on the exception type.

``` py
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)

```

Exception handlers don’t just handle exceptions if they occur immediately in the try clause, but also if they occur inside functions that are called (even indirectly) in the try clause. For example:

``` py
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

```

If a `finally` clause is present, the finally clause will execute as the last task before the try statement completes. 

``` py
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

# try these
divide(2, 1)
divide(2, 0)
divide("2", "1")
```

<sub> From [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) of python documentation. </sub>


#### The with statement

The context manager handles 
- the entry into, and 
- the exit from
- the desired runtime context 

for the execution of the block of code.

The with statement is used to wrap the execution of a block with methods defined by a context manager

``` py
with EXPRESSION as TARGET:
    SUITE
```

With more than one item, the context managers are processed as if multiple with statements were nested:

``` py
# same as below
with A() as a, B() as b:
    SUITE

# same as above
with A() as a:
    with B() as b:
        SUITE
```

How with works can be more read on [the with statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement) of python docs.

### Simple Statements

#### The assert statement
#### The pass statement
#### The del statement
#### The return statement
#### The yield statement
#### The raise statement
#### The break statement
#### The continue statement
#### The import statement
#### The global statement
#### The nonlocal statement

<!-- ## Expressions  -->