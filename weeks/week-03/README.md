# Week 3

What we will cover:

- Wrap Up from Previous Week
- Introduction to python. Learning python as general-purpose programming language. 
- Data Types

## Table of Contents

- [Week 3](#week-3)
  - [Table of Contents](#table-of-contents)
  - [Wrap Up](#wrap-up)
  - [Common Python Syntax](#common-python-syntax)
    - [Comments](#comments)
    - [Print](#print)
    - [Variables names](#variables-names)
      - [Rules](#rules)
      - [Conventions](#conventions)
    - [Reserved Keywords](#reserved-keywords)
  - [Python Data Model](#python-data-model)
    - [Object](#object)
    - [The standard type hierarchy](#the-standard-type-hierarchy)
      - [None](#none)
      - [NotImplemented](#notimplemented)
      - [Ellipsis](#ellipsis)
      - [numbers.Number](#numbersnumber)
      - [numbers.Integral](#numbersintegral)
      - [Sequences](#sequences)
        - [Immutable sequences](#immutable-sequences)
        - [Mutable sequences](#mutable-sequences)
      - [Set Types](#set-types)
      - [Mappings](#mappings)

## Wrap Up

- Installing python from python.org 
- Python Package Index for 3rd party packages
- What is PEP?
- How to install any package? Using `pip` to access many 3rd party packages
- Python virtual [environments](https://github.com/spu-python-203/class-materials/tree/main/weeks/week-02#environments)

## Common Python Syntax

### Comments

- Single line 
- Multiline

``` py
# single line comment

"""
Multiline
Comment
"""
```
### Print

Prints to console.

``` py
print('welcome')
```

### Variables names

There are rules, and conventions.

#### Rules

Variables names must start with a letter or an underscore, such as:

- _underscore
- underscore_

The remainder of your variable name may consist of letters, numbers and underscores.

- password1
- n00b
- underscores


Names are case sensitive.

- casesensitive, CASESENSITIVE, and Case_Sensitive are each a different variable.

#### Conventions

Readability is very important. Which of the following is easiest to read? I’m hoping you’ll say the first example.

- python_puppet
- pythonpuppet
- pythonPuppet

Descriptive names are very useful. If you are writing a program that adds up all of the bad puns made in this book, which do you think is the better variable name?

totalbadpuns
super_bad

Avoid using the lowercase letter ‘l’, uppercase ‘O’, and uppercase ‘I’. Why? Because the l and the I look a lot like each other and the number 1. And O looks a lot like 0.

Check out python naming convensions by [`PEP 0008`](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

### Reserved Keywords

As defined in reserved keywords in [Python documentation](https://docs.python.org/3/reference/lexical_analysis.html#keywords).

```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

## Python Data Model

Everything under data model is available without requiring any import of a package.
You don't have to define the variable type while writing python, like in other languages such as Java, etc.

### Object

Python defines data as objects. Objects are python's absraction for data. All data in a Python program is represented by objects or by relations between objects.

Every object has 
- an identity (An object’s identity never changes once it has been created)
- a type 
- a value.

How we compare two objects? Using `is` operator.
How we find the memory id representation of an object? `id()` function.

An object’s type determines the operations that the object supports (e.g., “does it have a length?”) and also defines the possible values for objects of that type. The `type()` function returns an object’s type (which is an object itself). Like its identity, an object’s type is also **unchangeable**. 

The value of some objects can change or cannot change. 

- Objects whose value can change are said to be **mutable**.
- Objects whose value is unchangeable once they are created are called **immutable**. 

<sub>Originated from [Objects, values and types](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)</sub>

### The standard type hierarchy

- None
- NotImplemented
- Ellipsis
- numbers.Number
- numbers.Integral
- Integers (int)
- Booleans (bool)
- numbers.Real (float)
- numbers.Complex (complex)


#### None

This type has a single value. There is a single object with this value. Its truth value is false.

``` py
a = None
```

#### NotImplemented

This type has a single value. There is a single object with this value. This object is accessed through the built-in name NotImplemented. Numeric methods and rich comparison methods should return this value if they do not implement the operation for the operands provided. 

``` py
def some_function():
    raise NotImplemented
```

#### Ellipsis

This type has a single value. There is a single object with this value. 
This object is accessed through the literal `...` or the built-in name `Ellipsis`. Its truth value is true.

``` py
>>> ...
Ellipsis
```

#### numbers.Number

These are created by numeric literals and returned as results by arithmetic operators and arithmetic built-in functions. 

Numeric objects are **immutable**; once created their value never changes. 

Some features of numbers in python:

- Python numbers are of course strongly related to mathematical numbers, but subject to the limitations of numerical representation in computers.
- Leading zeros, possibly excepting a single zero before a decimal point, are not shown.
- Trailing zeros, possibly excepting a single zero after a decimal point, are not shown.
- A sign is shown only when the number is negative.

Python distinguishes between integers, floating point numbers, and complex numbers:

#### numbers.Integral

These represent elements from the mathematical set of integers (positive and negative).

There are two types of integers:

Integers (int)

These represent numbers in an unlimited range, subject to available (virtual) memory only. For the purpose of shift and mask operations, a binary representation is assumed, and negative numbers are represented in a variant of 2’s complement which gives the illusion of an infinite string of sign bits extending to the left.

``` py
a = 23
b = 0
```

Booleans (bool)

These represent the truth values False and True. The two objects representing the values False and True are the only Boolean objects. The Boolean type is a subtype of the integer type, and Boolean values behave like the values 0 and 1.

``` py
my_boolean = False
```

numbers.Real (float)

These represent machine-level double precision floating point numbers. You are at the mercy of the underlying machine architecture (and C or Java implementation) for the accepted range and handling of overflow.

``` py
a = 2.23
```

#### Sequences

These represent finite ordered sets indexed by non-negative numbers. 

- The built-in function `len()` returns the number of items of a sequence. 
- When the length of a sequence is n, the index set contains the numbers 0, 1, …, n-1. Item i of sequence a is selected by a[i].
- Sequences also support slicing: a[i:j] selects all items with index k such that i <= k < j. When used as an expression, a slice is a sequence of the same type. This implies that the index set is renumbered so that it starts at 0.
- Some sequences also support “extended slicing” with a third “step” parameter: a[i:j:k] selects all items of a with index x where x = i + n*k, n >= 0 and i <= x < j.

Sequences are distinguished according to their **mutability**:

##### Immutable sequences

An object of an immutable sequence type cannot change once it is created. (If the object contains references to other objects, these other objects may be mutable and may be changed; however, the collection of objects directly referenced by an immutable object cannot change.)

The following types are immutable sequences:

**Strings**
A string is a sequence of values that represent Unicode code points. All the code points in the range U+0000 - U+10FFFF can be represented in a string. Python doesn’t have a char type; instead, every code point in the string is represented as a string object with length 1. 

- The built-in function `ord()` converts a Unicode code point from its string form to an integer in the range 0 - 10FFFF; 
- `chr()` converts an integer in the range 0 - 10FFFF to the corresponding length 1 string object. 
- `str.encode()` can be used to convert a str to bytes using the given text encoding 
- `bytes.decode()` can be used to achieve the opposite.

``` py
>>> a = 'my string'
>>> a[2:3]
' '
>>> a[2:5:2]
' t'
```

**Tuples**
The items of a tuple are arbitrary Python objects. 

- Tuples of two or more items are formed by comma-separated lists of expressions. 
- A tuple of one item (a ‘singleton’) can be formed by affixing a comma to an expression (an expression by itself does not create a tuple, since parentheses must be usable for grouping of expressions). 
- An empty tuple can be formed by an empty pair of parentheses.

``` py
>>> a = (2,3,4,5)
>>> a[2:3]
4
>>> len(a)
4
>>> b = 2, # singleton
(2,)
>>> b = ()
()
```

**Bytes**
A bytes object is an immutable array. 

- The items are 8-bit bytes, represented by integers in the range 0 <= x < 256. 
- Bytes literals (like b'abc') and the built-in `bytes()` constructor can be used to create bytes objects. Also, 
- Bytes objects can be decoded to strings via the decode() method.

``` py
str = "beginnersbook"

# encoding 'utf-8'
arr = bytes(str, 'utf-8')

#encdoing 'utf-16'
arr2 = bytes(str, 'utf-16')

print(arr)
print(arr2)
# b'beginnersbook'
# b'\xff\xfeb\x00e\x00g\x00i\x00n\x00n\x00e\x00r\x00s\x00b\x00o\x00o\x00k\x00'
```
##### Mutable sequences

Mutable sequences can be changed after they are created. The subscription and slicing notations can be used as the target of assignment and `del` (delete) statements.

There are currently two intrinsic mutable sequence types:

**Lists**
The items of a list are arbitrary Python objects. Lists are formed by placing a comma-separated list of expressions in square brackets. (Note that there are no special cases needed to form lists of length 0 or 1.)


``` py
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters

# replace some values
letters[2:5] = ['C', 'D', 'E']
letters

# now remove them
letters[2:5] = []
letters

# clear the list by replacing all the elements with an empty list
letters[:] = []
letters
```

A nested list example

``` py
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```

**Byte Arrays**
A bytearray object is a mutable array. They are created by the built-in `bytearray()` constructor. These almost provide the same interface and functionality as immutable bytes objects.

#### Set Types

These represent unordered, finite sets of unique, immutable objects. 

As such, they cannot be indexed by any subscript. However, they can be iterated over, and the built-in function `len()` returns the number of items in a set. 

Common uses for sets are 
- fast membership testing
- removing duplicates from a sequence
- computing mathematical operations such as intersection, union, difference, and symmetric difference.

For set elements, the same immutability rules apply as for dictionary keys. Note that numeric types obey the normal rules for numeric comparison: if two numbers compare equal (e.g., 1 and 1.0), only one of them can be contained in a set.

There are currently two intrinsic set types:

**Sets**
These represent **a mutable set**. They are created by the built-in `set()` constructor and can be modified afterwards by several methods, such as add().

``` py
myset = {"hi", 2, "bye", "Hello World"}

# checking whether 2 is in myset
print(2 in myset)
```
**Frozen sets**
These represent **an immutable set**. They are created by the built-in `frozenset()` constructor. As a frozenset is immutable and hashable, it can be used again as an element of another set, or as a dictionary key.


``` py
# Python program to understand use 
# of frozenset function 
  
# creating a dictionary  
Student = {"name": "John", "age": 21, "sex": "Male",  
           "college": "SPU", "address": "Jersey City"} 
  
# making keys of dictionary as frozenset 
key = frozenset(Student) 
  
# printing keys details 
print('The frozen set is:', key) 
```

#### Mappings

These represent finite sets of objects indexed by arbitrary index sets. 

The subscript notation `a[k]` selects the item indexed by `k from the mapping a`; this can be used in expressions and as the target of assignments or `del` statements. The built-in function `len()` returns the number of items in a mapping.

There is currently a single intrinsic mapping type:

**Dictionaries**
These represent finite sets of objects indexed by nearly arbitrary values. 

- The only types of values not acceptable as keys are values containing lists or dictionaries or other mutable types that are compared by value rather than by object identity, the reason being that the efficient implementation of dictionaries requires a key’s hash value to remain constant. 
- Numeric types used for keys obey the normal rules for numeric comparison: if two numbers compare equal (e.g., 1 and 1.0) then they can be used interchangeably to index the same dictionary entry.
- Dictionaries are mutable; they can be created by the {...} notation (see section Dictionary displays).

``` py
mydict = {'StuName': 'John', 'StuAge': 30, 'StuCity': 'Agra'}

print("Student Age is:", mydict['StuAge'])
print("Student City is:", mydict['StuCity'])

del mydict['StuCity']
```

<sub>Almost the same as [The standard type hierarchy](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy), with an addition of lists and code samples.</sub>
