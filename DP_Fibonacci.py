#O(n)

def fib(n):
    # Initialize an array to store the Fibonacci numbers
    fib_numbers = [1, 1]
    # Base case: If n is 1 or 2, return n
    if n < 2:
        return 1
    else:
    # Iterate from 2 to n
        for i in range(2, n):
            # Compute the next Fibonacci number
            fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])
    # Return the n-th Fibonacci number
    return fib_numbers[n-1]

print(fib(6))