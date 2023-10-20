# Working With Primes

A simple Python module for working with prime numbers, created by Munashe Mukweya.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
  - [firstNPrimes(n)](#firstnprimesn)
  - [isPrime(n)](#isprimen)
  - [differences(n)](#differencesn)
  - [sumOfPrimes(n)](#sumofprimesn)
  - [theNthPrime(n)](#thenthprimen)
  - [sumOfDifferences(n)](#sumofdifferencesn)
  - [primeCounting(n)](#primecountingn)
  - [lcm(n)](#lcmn)
  - [primeSlice(start, stop)](#primeslicestart-stop)
  - [primeDifferenceSlice(start, stop)](#primedifferenceslicestart-stop)
  - [modifyValues(array, operation, operand)](#modifyvaluesarray-operation-operand)
  - [randomPrimeSlice(start, stop, length)](#randomprimeslicestart-stop-length)
  - [randomDifferencesSlice(start, stop, length)](#randomdifferencesslicestart-stop-length)
  - [graphDifferences(n)](#graphdifferencesn)
  - [graphPrimes(stop, operation, operand, start)](#graphprimesstop-operation-operand-start)
  - [sacksSpiral(n, coordinateRange, dotSize)](#sacksspiraln-coordinaterange-dotsize)
  - [differenceSpiral(n, coordinateRange, dotSize)](#differencespiraln-coordinaterange-dotsize)
- [License](#license)

## Introduction

This Python module provides a collection of functions for visualizing and performing operations with prime numbers. It is a simple tool for mathematical analysis and educational purposes.

## Features

- Generate the first 'n' prime numbers.
- Calculate the differences between successive prime numbers.
- Check a number for primality
- Find the 'n'-th prime number.
- Perform mathematical operations on prime numbers.
- Visualize prime numbers using graphical representations, including Sacks Spiral and graphs.

## Installation

You can install this module using pip:

```
pip install wwp
```

## Usage

To use this module, you can import all functions...

```
from wwp import *
```

...or specific functions

```
from wwp import _function_name_
```

Then you can use the function/s provided in the module

## Functions

### firstNPrimes(n): 
Returns an array containing the first 'n' prime numbers along the number line.<br><br>
**Arguments**:<br>
n (int): The number of prime numbers to generate.<br><br>
**Returns**:<br>
list: A list of the first 'n' prime numbers. <br>
None: If 'n' is equal to 0.
### isPrime(n):
Returns True if 'n' is prime and False if it is not.<br><br>
**Arguments**:<br>
n (int): The number to check for primality.<br><br>
**Returns**:<br>
Boolean: True if 'n' is prime and False if it is not.<br>
None: If 'n' is equal to 0.
### differences(n):
Returns an array containing the differences between successive prime numbers up to the 'n'-th prime.<br><br>
**Arguments**:<br>
n (int): The number of prime numbers to consider for difference calculation.<br><br>
**Returns**:<br>
list: A list of the differences between successive prime numbers.<br>
None: If 'n' is equal to 0.
### sumOfPrimes(n):
Calculates the sum of the first 'n' prime numbers.<br><br>
**Arguments**:<br>
n (int): The first 'n' prime numbers to add up.<br><br>
**Returns**:<br>
int: The sum of the first n prime numbers.<br>
None: If 'n' is equal to 0.
### theNthPrime(n):
Returns the 'n'-th prime number.<br><br>
**Arguments**:<br>
n (int): The position of the prime number.<br><br>
**Returns**:<br>
int: The 'n'-th prime number.<br>
None: If 'n' is equal to 0.
### sumOfDifferences(n):
Calculates the sum of differences between the first 'n' prime numbers.<br><br>
**Arguments**:<br>
n (int): The first 'n' prime numbers to consider.<br><br>
**Returns**:<br>
int: The sum of the differences between the first 'n' prime numbers.<br>
None: If 'n' is equal to 0.
### primeCounting(n):
Returns the number of primes less than 'n'.<br><br>
**Arguments**:<br>
n (int): The positive integer for which you want to count the prime numbers less than it.<br><br>
**Returns**:<br>
int: The number of prime numbers less than 'n'.<br>
None: If 'n' is equal to 0.
### lcm(n):
Calculates the lowest common multiple of the first 'n' primes.<br><br>
**Arguments**:<br>
n (int): The first 'n' prime numbers to consider.<br><br>
**Returns**:<br>
int: The lowest common multiple of the first 'n' prime numbers<br>
None: If 'n' is equal to 0.
### primeSlice(start, stop):
Returns an array of prime numbers between 'start' and 'stop' (inclusive).<br><br>
**Arguments**:<br>
start (int): The starting integer for the range.<br>
stop (int): The ending integer for the range.<br><br>
**Returns**:<br>
list: A list of prime numbers within the inclusive range from 'start' to 'stop'.
### primeDifferenceSlice(start, stop):
Returns an array of the differences between successive prime numbers between 'start' and 'stop' (inclusive).<br><br>
**Arguments**:<br>
start (int): The starting integer for the range.<br>
stop (int): The ending integer for the range.<br><br>
**Returns**:<br>
list: A list of the differences between the prime numbers within the inclusive range from 'start' to 'stop'.
### modifyValues(array, operation, operand):
Modifies an array using the specified 'operation' and 'operand' values.<br><br>
**Arguments**:<br>
array (arr): An array of integer values.<br>
operation (str): The operation to perform on the prime numbers within the range. Valid values are "multiply" or "*", "divide" or "/", "subtract" or "-", "add" or "+", and "exponent" or "^".<br>
operand (int, float or expression): The value to use as the operand for the specified operation.<br><br>
**Returns**:<br>
list: A list of integers after applying the specified 'operation' and 'operand'.
### randomPrimeSlice(start, stop, length):
Generates a random selection of prime numbers within the inclusive range from 'start' to 'stop'.<br><br>
**Arguments**:<br>
start (int): The starting integer for the range.<br>
stop (int): The ending integer for the range.<br>
length (int): The number of prime numbers to include in the random selection.<br><br>
**Returns**:<br>
list: A list of prime numbers randomly selected from within the inclusive range between 'start' and 'stop'.<br>
None: 'length' is equal to 0.
### randomDifferencesSlice(start, stop, length): 
Generates a random selection of differences between successive prime numbers within the inclusive range from 'start' to 'stop'.<br><br>
**Arguments**:<br>
start (int): The starting integer for the range.<br>
stop (int): The ending integer for the range.<br>
length (int): The number of differences to include in the random range.<br><br>
**Returns**:<br>
list: A list of the differences between prime numbers randomly selected from within the inclusive range between 'start' and 'stop'.<br>
None: 'length' is equal to 0.  
### graphDifferences(n):
Graphs the differences between the first 'n' successive prime numbers.<br><br>
**Arguments**:<br>
n (int): The number of successive prime numbers to consider for generating the graph.<br><br>
**Returns**:<br>
This function doesn't return any value; it generates and displays a graph.<br>
None: if 'n' is equal to 0.
### graphPrimes(stop, operation, operand, start):
Plots and displays a graph comparing a set of regular and modified prime numbers.<br><br>
**Arguments**:<br>
stop (int): The ending integer for the range of primes.<br>
operation (str, optional): The mathematical operation to apply to the prime numbers. Valid values are "multiply" or "*", "divide" or "/", "subtract" or "-", "add" or "+", and "exponent" or "^". Defaults to addition ("+").<br>
operand (int, float, or expression, optional): The value to use as the operand for the specified operation. Defaults to 0.<br>
start (int, optional): The starting integer for the range. Defaults to 1.<br><br>
**Returns**:<br>
This function doesn't return any value; it generates and displays a graph.
### sacksSpiral(n, coordinateRange, dotSize):
Draws a Sacks Spiral representation of the first 'n' prime numbers.<br><br>
**Arguments**:<br>
n (int): The first 'n' prime numbers to consider for drawing the Sacks Spiral.<br>
coordinateRange (int, optional): The coordinate system's range for both axis. Defaults to 100.<br>
dotSize (int, optional): The size of dots representing the prime numbers. Defaults to 5.<br><br>
**Returns**:<br>
This function doesn't return any value; it generates and displays a drawing.
### differenceSpiral(n, coordinateRange, dotSize):
Draws a spiral using the same rules of the Sacks Spiral using non-repeating differences
between the primes instead of the primes themselves. Uses turtle graphics library.<br><br>
**Arguments**:<br>
n (int): The limit of differences to consider for drawing the spiral.<br>
coordinateRange (int, optional): The coordinate system's range for both axis. Defaults to 15.<br>
dotSize (int, optional): The size of dots representing the differences. Defaults to 10.<br><br>
**Returns**:<br>
 This function doesn't return any value; it generates and displays a graph.

## License

This project is licensed under the MIT License - see the [LICENSE](workingWithPrimes/LICENSE.txt) file for details.

