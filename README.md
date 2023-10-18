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

* **firstNPrimes(n)**: Returns an array containing the first 'n' prime numbers.
* **differences(n)**: Returns an array containing the differences between successive prime numbers up to the 'n'-th prime.
* **sumOfPrimes(n)**: Calculates the sum of the first 'n' prime numbers.
* **theNthPrime(n)**: Returns the 'n'-th prime number.
* **sumOfDifferences(n)**: Calculates the sum of differences between the first 'n' prime numbers.
* **primeCounting(n)**: Returns the number of primes less than 'n'.
* **lcm(n)**: Calculates the lowest common multiple of the first 'n' primes.
* **primeSlice(start, stop)**: Returns an array of prime numbers between 'start' and 'stop' (inclusive).
* **primeDifferenceSlice(start, stop)**: Returns an array of the differences between successive prime numbers between 'start' and 'stop'.
* **modifyPrime(operation, operand, stop, start=1)**: Modifies an array of prime numbers using the specified operation and operand.
* **randomRange(start, stop, length)**: Generates a random selection of prime numbers within the inclusive range from 'start' to 'stop'.
* **randomDifferencesRange(start, stop, length)**: Generates a random selection of differences between successive prime numbers within the inclusive range from 'start' to 'stop'.
* **graphDifferences(n)**: Graphs the differences between the first 'n' successive prime numbers.
* **graphPrimes(stop, operation, operand, start)**: Plots and displays a graph comparing regular and modified prime numbers.
* **sacksSpiral(n, coordinateRange=100, dotSize=5)**: Draws a Sacks Spiral representation of the first 'n' prime numbers.

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

