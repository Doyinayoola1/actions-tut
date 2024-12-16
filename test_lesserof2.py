"""
This module contains unit tests for the `lesser_of_two` function.

The `lesser_of_two` function compares two numbers and returns the lesser of the two.
"""
#This checks lesser file
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    
    return max(a,b)
