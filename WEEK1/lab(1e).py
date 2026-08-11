# Recursive function to find the nth Fibonacci number
def fibonacci(n):
    # Base cases: the 0th term is 0, and the 1st term is 1
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive step: Fn = Fn-1 + Fn-2
    return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage: Print the first 7 terms
N = 7
print(f"The first {N} terms of the Fibonacci series are:")

for i in range(N):
    # Print each term separated by a space
    print(fibonacci(i), end=" ")
