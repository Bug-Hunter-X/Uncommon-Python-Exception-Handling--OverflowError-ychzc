def function_with_uncommon_error(x):
    try:
        result = 1 / x
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input type"

#Example usage:
print(function_with_uncommon_error(0)) #Outputs: Division by zero
print(function_with_uncommon_error(2)) #Outputs: 0.5
print(function_with_uncommon_error('a')) #Outputs: Invalid input type
print(function_with_uncommon_error(0.0)) #Outputs: Division by zero

#The uncommon part:
# The function handles both ZeroDivisionError and TypeError in an expected way. However, it does not handle other potential errors such as OverflowError,
#which can occur with very large numbers or floating-point exceptions.  This leads to potential issues for large inputs or values close to the machine's
#numerical limits.