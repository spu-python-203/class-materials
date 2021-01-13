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
  - [Expressions](#expressions)

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

``` py
```

### Comparison Operator (==, !=, >, <, >=, <=)

``` py
```

### Logical Operators (and, or, not)

``` py
```

### Identity Operators (is, is not)

``` py
```

### Membership Operators (in, not in)

``` py
```

## Execution Model

### Control Flow

#### The if statement
#### The while statement
#### The for statement
#### The try statement
#### The with statement

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

## Expressions 