# Working With Primes

A simple Python module for working with prime numbers, created by Munashe Mukweya.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [License](#license)

## Introduction

This Python module provides a collection of functions for visualizing and performing various operations with prime numbers. It is a simple tool for mathematical analysis and educational purposes.

## Features

- Generate the first 'n' prime numbers.
- Calculate the differences between successive prime numbers.
- Find the 'n'-th prime number.
- Perform mathematical operations on prime numbers.
- Visualize prime numbers using graphical representations, including Sacks Spiral and graphs.

## Installation

You can install this module using pip:

```
pip install wwp
```

## Usage

To use this module, import it in your Python script:

```
import wwp
```

Then you can use the functions provided in the module

## Functions

### firstNPrimes(n): 
Returns an array containing the first 'n' prime numbers along the number line.
#### Arguments:
n (int): The number of prime numbers to generate.
#### Returns:
list: A list of the first 'n' prime numbers. <br>
None: If 'n' is less than or equal to 0.
### differences(n):
Returns an array containing the differences between successive prime numbers up to the 'n'-th prime.
#### Arguments:
n (int): The number of prime numbers to consider for difference calculation.
#### Returns:
list: A list of the differences between successive prime numbers.<br>
None: If 'n' is less than or equal to 0. 
### sumOfPrimes(n):
Calculates the sum of the first 'n' prime numbers.
#### Arguments:
n (int): The first 'n' prime numbers to add up.
#### Returns:
int: The sum of the first n prime numbers.<br>
None: If 'n' is less than or equal to 0.
### theNthPrime(n):
Returns the 'n'-th prime number.
#### Arguments:
n (int): The position of the prime number.
#### Returns:
int: The 'n'-th prime number.<br>
None: If 'n' is less than or equal to 0.
### sumOfDifferences(n):
Calculates the sum of differences between the first 'n' prime numbers.
#### Arguments:
n (int): The first 'n' prime numbers to consider.
#### Returns:
int: The sum of the differences between the first 'n' prime numbers.<br>
None: If 'n' is less than or equal to 0.
### primeCounting(n):
Returns the number of primes less than 'n'.
#### Arguments:
n (int): The positive integer for which you want to count the prime numbers less than it.
#### Returns:
int: The number of prime numbers less than 'n'.<br>
None: If 'n' is less than or equal to 0.
### lcm(n):
Calculates the lowest common multiple of the first 'n' primes.
#### Arguments:
n (int): The first 'n' prime numbers to consider.
#### Returns:
int: The lowest common multiple of the first 'n' prime numbers<br>
None: If 'n' is less than or equal to 0.
### primeSlice(start, stop):
Returns an array of prime numbers between 'start' and 'stop' (inclusive).
#### Arguments:
start (int): The starting integer for the range.<br>
stop (int): The ending integer for the range.
#### Returns:
list: A list of prime numbers within the inclusive range from 'start' to 'stop'.<br>
None: If 'start' or 'stop' is less than or equal to 0.
### primeDifferenceSlice(start, stop):
Returns an array of the differences between successive prime numbers between 'start' and 'stop'.
#### Arguments:
start (int): The starting integer for the range.<br>
stop (int): The ending integer for the range.
#### Returns:
list: A list of the differences between the prime numbers within the inclusive range from 'start' to 'stop'.<br>
None: If 'start' or 'stop' is less than or equal to 0.
### modifyValues(array, operation, operand):
Modifies an array using the specified 'operation' and 'operand' values.
#### Arguments:
array (arr): An array of integer values.
operation (str): The operation to perform on the prime numbers within the range. Valid values are "multiply" or "*", "divide" or "/", "subtract" or "-", "add" or "+", and "exponent" or "^".<br>
operand (int, float or expression): The value to use as the operand for the specified operation.<br>
#### Returns:
list: A list of integers after applying the specified 'operation' and 'operand'.
### randomRange(start, stop, length):
Generates a random selection of prime numbers within the inclusive range from 'start' to 'stop'.
#### Arguments:
start (int): The starting integer for the range.<br>
stop (int): The ending integer for the range.<br>
length (int): The number of prime numbers to include in the random selection.
#### Returns:
list: A list of prime numbers randomly selected from within the inclusive range between 'start' and 'stop'.<br>
None: If 'start' or 'stop' is less than or equal to 0.
### randomDifferencesRange(start, stop, length): 
Generates a random selection of differences between successive prime numbers within the inclusive range from 'start' to 'stop'.
#### Arguments:
start (int): The starting integer for the range.<br>
stop (int): The ending integer for the range.<br>
length (int): The number of differences to include in the random range.
#### Returns:
list: A list of the differences between prime numbers randomly selected from within the inclusive range between 'start' and 'stop'.<br>
None: If 'start' or 'stop' is less than or equal to 0.  
### graphDifferences(n):
Graphs the differences between the first 'n' successive prime numbers.
#### Arguments:
n (int): The number of successive prime numbers to consider for generating the graph.
#### Returns:
This function doesn't return any value; it generates and displays a graph.<br>
None: if 'n' is less or equal to 0.
### graphPrimes(stop, operation, operand, start):
Plots and displays a graph comparing regular and modified prime numbers.
#### Arguments:
stop (int): The ending integer for the range of primes.<br>
operation (str, optional): The mathematical operation to apply to the prime numbers. Valid values are "multiply" or "*", "divide" or "/", "subtract" or "-", "add" or "+", and "exponent" or "^". Defaults to addition ("+").<br>
operand (int, float, or expression, optional): The value to use as the operand for the specified operation. Defaults to 0.<br>
start (int, optional): The starting integer for the range. Defaults to 1.
#### Returns:
This function doesn't return any value; it generates and displays a graph.<br>
None: If 'start' or 'stop' is less than or equal to 0.
### sacksSpiral(n, coordinateRange=100, dotSize=5):
Draws a Sacks Spiral representation of the first 'n' prime numbers.
#### Arguments:
n (int): The first 'n' prime numbers to consider for drawing the Sacks Spiral.<br>
coordinateRange (int, optional): The coordinate system's range for both axis. Defaults to 100.<br>
dotSize (int, optional): The size of dots representing the prime numbers. Defaults to 5.
#### Returns:
This function doesn't return any value; it generates and displays a drawing.<br>
None: If n is less than or equal to 0.

## License

This project is licensed under the MIT License - see the [LICENSE](wwp/LICENSE.txt) file for details.

