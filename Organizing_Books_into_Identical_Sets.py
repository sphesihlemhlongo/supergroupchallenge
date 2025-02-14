from math import gcd
from functools import reduce
from collections import Counter

def can_organize_books(shelf):
    counts = list(Counter(shelf).values())
    return "YES" if reduce(gcd, counts) > 1 else "NO"

# Test Cases
print(can_organize_books([5, 5, 3, 3, 2, 2]))  # YES
print(can_organize_books([1,2,3,4,4,3,2,1]))  # YES

# Test for:
print(can_organize_books([1234567, 1234567, 2345678, 2345678, 3456789, 3456789, 1234567, 2345678, 
                          3456789, 4567890, 4567890, 5678901, 5678901, 6789012, 6789012, 1234567, 
                          2345678, 3456789, 4567890, 5678901, 4567890, 5678901]))  # Output?
