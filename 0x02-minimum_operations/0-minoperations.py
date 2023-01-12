#!/usr/bin/python3
"""
n a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """
    method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file
    """
    if type(n) != int:
        return 0

    char = 1
    operator = 0
    memory_copy = 0

    while char < n:
        if n % char == 0:
            memory_copy = char
            operator += 1
            char *= 2
            operator += 1

        else:
            char += memory_copy
            operator += 1

    return operator
