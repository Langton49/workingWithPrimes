'''
This Python module provides a collection of functions for working with prime numbers.
It includes functionalities such as generating the first 'n' prime numbers, calculating the differences between
successive prime numbers, finding the 'n'-th prime number, performing mathematical operations on prime numbers, and
visualizing prime numbers in various ways, including drawing Sacks Spiral representations and plotting graphs.
The module uses external libraries like turtle and matplotlib for graphical representations.

Disclaimer:
- To use the graphing functions, such as `graphDifferences` and `graphPrimes` function, 
  ensure the following libraries have been installed on your system:
  
  1. Matplotlib (for graphing):
     You can install it with:
     
     pip install matplotlib
     

  2. Numpy (for data manipulation):
     You can install it with:
     
     pip install numpy
     

By Munashe Mukweya
'''

import random
import turtle
from math import *
import matplotlib.pyplot as plt
import numpy as np

def firstNPrimes(n):
    '''
    Returns an array containing the first 'n' prime numbers along the number line.

    Args:
        n (int): The number of prime numbers to generate.

    Returns:
        list: A list of the first 'n' prime numbers.
        None: If 'n' is less than or equal to 0.
    '''
    if n <= 0:
        return None
    primes = [2]
    num = 3
    while len(primes) < n:
        isPrime = True
        for j in range(len(primes)):
            if primes[j]**2 > num:
                break
            if  num%primes[j]==0:
                isPrime = False
                break
        if isPrime:
            primes.append(num)
        num += 2
    return primes

def differences(n):
    '''
    Calculates the differences between successive prime numbers up to the 'n'-th prime number.

    Args:
        n (int): The number of prime numbers to consider for difference calculation.

    Returns:
        list: A list of the differences between successive prime numbers.
        None: If 'n' is less than 0. 
    '''
    if n<0:
        return None
    primes = firstNPrimes(n)
    primeDifferences = []
    for i in range(len(primes)):
        if i != 0:
            primeDifferences.append(primes[i] - primes[i-1])
    return primeDifferences

def theNthPrime(n):
    '''
    Returns the 'n'-th prime along the number line.

    Args:
        n (int): The position of the prime number.

    Returns:
        int: The 'n'-th prime number.
        None: If 'n' is less than or equal to 0.
    '''
    if n <= 0:
        return None
    primes = firstNPrimes(n)
    return primes[n-1]

def sumOfDifferences(n):
    '''
    Calculates the sum of the differences between the first 'n' prime numbers.

    Args:
        n (int): The number of prime numbers to consider.

    Returns:
        int: The sum of the differences between the first 'n' prime numbers.
        None: If 'n' is less than or equal to 0.
    '''
    if n <= 0:
        return None
    return theNthPrime(n)-2

def sumOfPrimes(n):
    '''
    Calculates the sum of the first 'n' primes along the number line.

    Args:
        n (int): The first 'n' prime numbers to add up.

    Returns:
        int: The sum of the first n prime numbers.
        None: If 'n' is less than or equal to 0.
    '''
    if n <= 0:
        return None
    primes = firstNPrimes(n)
    total = 0
    for i in range(n):
        total = total + primes[i]
    return total

def primeCounting(n):
    '''
    Returns the number of primes less than 'n'.

    Args:
        n (int): The positive integer for which you want to count the prime numbers less than it.

    Returns:
        int: The number of prime numbers less than 'n'.
        None: If 'n' is less than or equal to 0.
    '''
    if n<=0:
        return None
    total = 0
    primes = firstNPrimes(n)
    for i in primes:
        if i < n:
            total+=1
    return total

def lcm(n):
    '''
    Calculates the lowest common multiple of the first 'n' primes.

    Args:
        n (int): The first 'n' prime numbers to consider.

    Returns:
        int: The lowest common multiple of the first 'n' prime numbers
        None: If 'n' is less than or equal to 0.
    '''
    if n <= 0:
        return None
    lowestcm = 2
    primes = firstNPrimes(n)
    for i in range(1, n):
        lowestcm = lowestcm * primes[i]
    return lowestcm

def primeSlice(start, stop):
    '''
    Returns an array of prime numbers between 'start' and 'stop' (inclusive).

    Args:
        start (int): The starting integer for the range.
        stop (int): The ending integer for the range.

    Returns:
        list: A list of prime numbers within the inclusive range from 'start' to 'stop'.
        None: If 'start' or 'stop' is less than or equal to 0.
    '''
    if start<=0 or stop<=0:
        return None
    primes = firstNPrimes(stop)
    slicedPrimes = []
    slicedPrimes[:stop-start] = primes[start-1:stop+1]
    return slicedPrimes

def primeDifferenceSlice(start, stop):
    '''
    Returns an array of the differences between successive prime numbers along the
    number line between 'start' and 'stop' (inclusive).

    Args:
        start (int): The starting integer for the range.
        stop (int): The ending integer for the range.

    Returns:
        list: A list of the differences between the prime numbers within the inclusive range from 'start' to 'stop'.
        None: If 'start' or 'stop' is less than or equal to 0.
    '''
    if start<=0 or stop<=0:
        return None
    primes = differences(stop)
    slicedPrimes = []
    slicedPrimes[:stop-start] = primes[start-1:stop+1]
    return slicedPrimes

def modifyValues(array, operation, operand):
    '''
    Modifies an array using the specified 'operation' and 'operand'
    values. Valid 'operation' values are "multiply" or "*", "divide" or "/",
    "subtract" or "-", "add" or "+", and "exponent" or "^".

    Args:
        array (arr): An array of integer values.
        operation (str): The operation to perform on the prime numbers within the range. Valid values are "multiply" or "*", "divide" or "/", "subtract" or "-", "add" or "+", and "exponent" or "^".
        operand (int, float or expression): The value to use as the second operand for the specified operation.

    Returns:
        list: A list of integers after applying the specified 'operation' and 'operand'.
    '''
    primes = array
    for i in range(len(primes)):
        if operation == "multiply" or operation == "*":
            primes[i] = primes[i] * operand
        elif operation == "divide" or operation == "/" and operand != 0:
            primes[i] = primes[i] / operand
        elif operation == "subtract" or operation == "-":
            primes[i] = primes[i] - operand
        elif operation == "add" or operation == "+":
            primes[i] = primes[i] + operand
        elif operation == "exponent" or operation == "^":
            primes[i] = primes[i] ** operand
        else:
            return "Undefined Function"
    return primes

def randomRange(start, stop, length):
    '''
    Generates a random selection of prime numbers within the inclusive
    range from 'start' to 'stop'. The 'length' parameter specifies the number
    of prime numbers to include in the random selection.

    Args:
        start (int): The starting integer for the range.
        stop (int): The ending integer for the range.
        length (int): The number of prime numbers to include in the random range.

    Returns:
         list: A list of prime numbers randomly selected from within the inclusive range between 'start' and 'stop'.
         None: If 'start' or 'stop' is less than or equal to 0.
    '''
    if start<=0 or stop<=0:
        return None
    primes = primeSlice(start, stop)
    furtherSlice = []*length
    randomIndex = random.randint(start, stop-length)
    furtherSlice[:length] = primes[randomIndex:randomIndex+length]
    return furtherSlice

def randomDifferencesRange(start, stop, length):
    '''
    Generates a random selection of differences between successive prime numbers within
    the inclusive range from 'start' to 'stop'. The 'length' parameter specifies the
    number of prime numbers to include in the random selection.

    Args:
        start (int): The starting integer for the range.
        stop (int): The ending integer for the range.
        length (int): The number of prime numbers to include in the random range.

    Returns:
        list: A list of the differences between prime numbers randomly selected from within the inclusive range between 'start' and 'stop'.
        None: If 'start' or 'stop' is less than or equal to 0.  
    '''
    if start<=0 or stop<=0:
        return None
    primes = primeDifferenceSlice(start, stop)
    furtherSlice = []*length
    randomIndex = random.randint(start, stop-length)
    furtherSlice[:length] = primes[randomIndex:randomIndex+length]
    return furtherSlice

def graphDifferences(n):
    '''
    Graphs the differences between the first 'n' successive prime numbers
    using matplotlib.pyplot.

    Args:
        n (int): The number of successive prime numbers to consider for generating the graph.

    Returns:
        This function doesn't return any value; it generates and displays a graph.
        None: if 'n' is less or equal to 0.
    '''
    if n<=0:
        return None
    primes = np.array(differences(n))
    plt.plot(primes)
    plt.xlabel('Number Line')
    plt.ylabel(f"Difference Between Prime Numbers")
    plt.title(f"Graph of Differences Between the First {n} Successive Prime Numbers")
    plt.show()
 
def graphPrimes(stop, operation="+", operand=0, start=1):
    '''
    Plots and displays a matplotlib.pyplot graph comparing two sets of
    prime numbers: regular prime numbers and modified prime numbers obtained
    by applying a specified mathematical operation. A modified graph is optional.

    Args:
        stop (int): The ending integer for the range of primes.
        operation (str, optional): The mathematical operation to apply to the prime numbers. Valid values are "multiply" or "*", "divide" or "/", "subtract" or "-", "add" or "+", and "exponent" or "^". Defaults to addition ("+").
        operand (int, float or expression, optional): The value to use as the second operand for the specified operation. Defaults to 0.
        start (int, optional): The starting integer for the range. Defaults to 1.

    Returns:
        This function doesn't return any value; it generates and displays a graph or set of graphs.
        None: If 'start' or 'stop' is less than or equal to 0.
    '''
    if stop<=0 or start<=0:
        return None
    primes1 = np.array(primeSlice(start, stop))
    if operand == 0:
        plt.plot(primes1, color='red', label='Parent Prime')
    else:
        primes2 = np.array(modifyValues(primeSlice(start, stop), operation, operand))
        plt.plot(primes1, color='red', label='Parent Prime')
        plt.plot(primes2, color='blue', label='Modified Prime')
    plt.xlabel('Number Line')
    plt.ylabel('Prime Numbers')
    plt.legend()
    plt.title('Graph of parent prime function and modified prime function')
    plt.show()

def sacksSpiral(n, coordinateRange=100, dotSize=5):
    '''
    Draws a Sacks Spiral representation of prime numbers up to a specified limit 'n' using the
    turtle graphics library. Takes time to complete for large values of 'n'.

    Args:
        n (int): The limit of prime numbers to consider for drawing the Sacks Spiral.
        coordinateRange (int, optional): The coordinate system's range for both axis. Defaults to 100.
        dotSize (int, optional): The size of dots representing the prime numbers. Defaults to 5.

    Returns:
        This function doesn't return any value; it generates and displays a graph.
        None: If n is less than or equal to 0.

     Disclaimer:
        - (If using IDLE or a Python shell) Please do not close the turtle graphics window manually before the function completes its execution. Closing the window prematurely may result in the "turtle.Terminator" error.
 
    '''
    if n<=0:
        return None
    turtle.setworldcoordinates(-coordinateRange, -coordinateRange, coordinateRange, coordinateRange)
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.hideturtle()
    t.speed("fastest")
    primes = firstNPrimes(n)
    for i in range(n):
        i = primes[i]
        theta = 2 * pi * sqrt(i)
        r = sqrt(i)
        x = cos(theta) * r
        y = -sin(theta) * r
        t.color("black")
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(dotSize)
    turtle.done()
