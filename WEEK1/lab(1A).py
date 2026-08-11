def countdown(n):
    # Base case: when countdown reaches 0, launch the rocket
    if n == 0:
        print("LAUNCH")
        return

    # Action: print the current countdown number
    print(n)

    # Recursive step: call the function with the next lower number
    countdown(n - 1)


# Example usage: Countdown from 5
countdown(10)
