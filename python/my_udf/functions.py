from __future__ import print_function
import sys
import math

def square(s):
  return s * s * s

def isprime(n):
  if n <= 1:
    return False
  elif n == 2:
    return True
  else:
    return not list(filter(lambda x: n % x == 0, range(3, int(math.sqrt(n)))))
