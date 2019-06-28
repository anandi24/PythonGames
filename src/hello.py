#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys
import re

def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s * 3
    if exclaim:
        result = result + '!!!'
    return result

# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.

  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    name = 'World'
    print('Hello', name)
    print('yay!')
    print(repeat('Anandi', True))
    print( len(repeat('Arey', True)))
    print(37//9)
    
    sample = 'Hello World'
    print(sample.isspace())
    print(sample[0:-6])

    def f():
        return True, False
    x, y = f()
    print(x)
    print(y)

    strs = ['ccc', 'aaaa', 'd', 'bb']
    print(sorted(strs, key=len))

    strs1 = ['xc', 'zb', 'yd' ,'wa']
    def MyFn(s):
        return s[-1]

    nums = [3,2,3,4,2,2,3,1]
    nums[:4]
    print(nums)
    list = []

    for num in nums:
        if not(num in list):
          list.append(num)
    print(list)

    print(sorted(strs1, key=MyFn))
    strs.remove('ccc')
    print(strs)
       ## "key" argument specifying str.lower function to use for sorting
#    print(sorted(strs, key=str.lower)) ## ['aa', 'BB', 'CC', 'zz'])
    j = '12'
    val = eval(j)

    print val
    print val + 5

    str = 'an example word:cat!!'
    match = re.search(r'word:\w\w\w', str)
    # If-statement after search() tests if it succeeded
    if match:
        print 'found', match.group() ## 'found word:cat'
    else:
        print 'did not find'
    match1 = re.search(r'iii', 'piiig')
    if match1:
        print 'found', match1.group()
    match2 = re.search(r'igs', 'piiig')
    if not match2:
        print 'not found', match2

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()