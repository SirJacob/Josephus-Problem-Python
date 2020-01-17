# Prompt: The Josephus Problem
# There is a circle of soldiers about to be captured.
# To avoid capture, each soldier kills the one next to them, which leaves one solider alive at the end.
# Given n, the number of soldiers present, find the position of the soldier that will be the last alive.

# Given n soldiers, calculate which will be last alive
def solve(n):
    # On a prime factor of two, the first soldier is always the last alive
    if prime_factor_of_two(n) != 0:
        return 1
    difference = n - pow(2, biggest_pow(n))
    return 2 * difference + 1


# Given input n, recurse and find the factor of two
# assumed no input <= 0
# Example: input: 8, logic: 2^3 = 8, output: power of 3
# If not a prime factor of two, output = 0
def prime_factor_of_two(n, count=0):
    if n == 2:
        return count + 1
    elif (n / 2) % 2 == 0:  # even
        return prime_factor_of_two(n / 2, count + 1)
    else:
        return 0


# Finds the largest power of two (2^x) that can fit in a number
# Example: input: 9, logic: 2^3 = 8, output: 3 is the greatest pow of two that can fit inside 9
def biggest_pow(n):
    pow_of_two = 0
    while n >= pow(2, pow_of_two):
        pow_of_two += 1
    return pow_of_two - 1


print('The Josephus Problem')
print('Input\t\tSolution')
soldier = 1
while soldier <= 41:
    solution = solve(soldier)
    print(f"{soldier}\t\t\t{solution}")
    soldier += 1
