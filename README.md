# Uncommon Python Exception Handling: OverflowError

This repository demonstrates a Python function that handles common exceptions (ZeroDivisionError, TypeError) during division. However, it overlooks less frequent exceptions such as OverflowError.  This can lead to unexpected crashes or incorrect results when dealing with extremely large numbers.

The `bug.py` file contains the original code, showcasing the incomplete exception handling.  The `bugSolution.py` file provides an improved version that addresses this oversight by adding comprehensive exception handling for more robust error management.

## How to run the code

1.  Clone this repository.
2.  Run `bug.py` and `bugSolution.py` using a Python interpreter.
3.  Observe the different outputs and error handling for various inputs, including edge cases such as extremely large numbers.