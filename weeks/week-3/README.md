# Week 3

What we will cover:

- Wrap Up from Previous Week
- Introduction to python. Learning python as general-purpose programming language. 
- Data Types

## Table of Contents

- [Week 3](#week-3)
  - [Table of Contents](#table-of-contents)
  - [Wrap Up](#wrap-up)
  - [Python Data Model](#python-data-model)
    - [Object](#object)
    - [The standard type hierarchy](#the-standard-type-hierarchy)
      - [None](#none)
      - [NotImplemented](#notimplemented)
      - [Ellipsis](#ellipsis)
      - [numbers.Number](#numbersnumber)
      - [numbers.Integral](#numbersintegral)
      - [Sequences](#sequences)
      - [Set Types](#set-types)
      - [Mappings](#mappings)

## Wrap Up

- Installing python from python.org 
- Python Package Index for 3rd party packages
- How to install any package? Using `pip` to access many 3rd party packages
- Python virtual [environments](https://github.com/spu-python-203/class-materials/tree/main/weeks/week-02#environments)

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
#### Set Types
#### Mappings
