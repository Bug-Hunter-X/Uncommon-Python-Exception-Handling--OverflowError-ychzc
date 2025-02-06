def function_with_improved_error_handling(x):
    try:
        result = 1 / x
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input type"
    except OverflowError:
        return "Numerical overflow"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

#Example Usage:
print(function_with_improved_error_handling(0)) #Outputs: Division by zero
print(function_with_improved_error_handling(2)) #Outputs: 0.5
print(function_with_improved_error_handling('a')) #Outputs: Invalid input type
print(function_with_improved_error_handling(float('inf'))) #Outputs: 0.0
print(function_with_improved_error_handling(float('nan'))) #Outputs: nan

#The improved part:
# The function now includes exception handling for OverflowError.  It also catches any other unexpected exceptions using a generic Exception clause,
#providing more informative error messages. This makes the function more robust and less prone to unexpected crashes.