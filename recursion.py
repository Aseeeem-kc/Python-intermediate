# Recursion

# Finding Factorial
# Non-recursive way

"""
Factorial is a mathematical operation that multiplies a given number by all positive integers less than itself.
For example, 5! (factorial of 5) = 5 * 4 * 3 * 2 * 1 = 120.
There are two common ways to calculate a factorial: iteratively and recursively.
"""

n = 7  # We want to find the factorial of 7.
fact = 1  # Start with 1 because multiplying by 1 does not change the result.

"""
This loop will keep multiplying fact by n and then decreasing n until n becomes 0.
When n reaches 0, the loop ends, and fact contains the factorial of the original number.
"""
while n > 0:
    fact = fact * n  # Multiply current fact by n.
    n -= 1  # Decrease n by 1 to eventually reach the base case.

print(fact)  # Output the result, which is the factorial of 7.

# Recursive way

"""
The recursive approach uses the concept of a function calling itself to solve a problem.
A base case is necessary to stop the recursion and prevent infinite loops.
"""

def factorial(n):
    if n < 1:  # Base case: if n is 0 or less, return 1 because 0! = 1.
        return 1
    else:
        """
        Recursive case: n! = n * (n-1)!
        This line calls the factorial function with n-1 until n reaches 0.
        """
        number = n * factorial(n-1)
        return number  # The recursion unwinds, multiplying the numbers in reverse order.

print(factorial(7))  # This will also print the factorial of 7.

"""
Explanation:
In recursion, each function call is stored in the call stack until the base case is reached.
After that, the stack unwinds, and the results are multiplied together.
"""

# Fibonacci Sequence
# Iterative way

"""
The Fibonacci sequence is a series where each number is the sum of the two preceding ones.
The sequence starts with 0 and 1 and proceeds as 0, 1, 1, 2, 3, 5, 8, 13, ...
"""

def fibonacci(n):
    a, b = 0, 1  # Start with the first two numbers in the sequence.

    """
    Loop to calculate the nth Fibonacci number.
    Each iteration moves to the next number in the sequence by updating a and b.
    """
    for x in range(n):
        a, b = b, a + b  # Update a to the next number and b to the sum of the last two.

    return a  # Return the nth Fibonacci number.

print(fibonacci(500))  # This efficiently computes and prints the 500th Fibonacci number.

"""
Explanation:
The iterative approach is more efficient than the recursive one for Fibonacci, as it avoids repeated calculations.
"""

# Recursive way

"""
The recursive method is simpler but less efficient for large numbers, as it involves many repeated calculations.
"""

def fibonacci2(n):
    if n <= 1:  # Base case: return n if it is 0 or 1, as these are the first two numbers in the sequence.
        return n
    else:
        # Recursive case: return the sum of the two previous Fibonacci numbers.
        return (fibonacci2(n-1) + fibonacci2(n-2))

"""
Warning:
Calculating fibonacci2(500) is extremely inefficient and will take a long time due to the exponential growth in function calls.
It’s generally impractical to use the recursive method for large n unless optimized (e.g., with memoization).
"""
print(fibonacci2(500))  # This is not practical for large numbers due to its inefficiency.

"""
Additional Explanation:
The recursive Fibonacci function has an exponential time complexity of O(2^n) due to the redundant calculations,
whereas the iterative method has a linear time complexity of O(n), making it much more suitable for large inputs.
"""

"""
General Note:
Recursion is powerful but should be used with caution for large problems or where performance is critical.
Understanding the difference between recursion and iteration is crucial for efficient algorithm design.
"""
