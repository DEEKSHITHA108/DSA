def calculate_growth_factor(p, n):
    if n == 0:
        return 1.0
    return p * calculate_growth_factor(p, n - 1)


# You MUST wrap the function call in print() to see the calculated result
result = calculate_growth_factor(1.05, 4)
print(result)
