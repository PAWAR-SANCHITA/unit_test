# to write test case function to for shopping item count.
# create function 

import sys
import os

# using pytest testing i set path for main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

def shopping_count(sum):
    return len(sum)