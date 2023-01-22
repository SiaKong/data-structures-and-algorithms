#O(n)

def fib(n):
    # Initialize an array to store the Fibonacci numbers
    fib_numbers = [0, 1]
    # Base case: If n is 0 or 1, return n
    if n < 2:
        return n
    # Iterate from 2 to n
    for i in range(2, n + 1):
        # Compute the next Fibonacci number
        fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])
    # Return the n-th Fibonacci number
    return fib_numbers[n]