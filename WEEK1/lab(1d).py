def calculate_arrangements(n):
    # Base case: 0! or 1! is always 1 way
    if n == 0 or n == 1:
        return 1

    # Recursive step: n! = n * (n - 1)!
    return n * calculate_arrangements(n - 1)


# Example usage: Arrange 5 parcels
parcels = 5
total_ways = calculate_arrangements(parcels)

# Wrap the result in a print statement to show the output
print(f"Total ways to arrange {parcels} parcels: {total_ways}")
