# Prompt: The Josephus Problem
# There is a circle of soldiers about to be captured.
# To avoid capture, each soldier kills the one next to them, which leaves one solider alive at the end.
# Given n, the number of soldiers present, find the position of the soldier that will be the last alive.

# This file uses a bit moving trick to cut out a lot of the computation involved in the solver.py file
# By converting the number of soldiers into binary and then taking the left-most bit and making it the right-most bit,
# and then converting that number back into decimal, we can find the solution much faster.

print('The Josephus Problem')
print('Input\t\tSolution')
soldier = 1
while soldier <= 41:
    if soldier == 1:
        solution = 1
    else:
        # Move first bit to the end
        binary_list = list(bin(soldier))
        binary_list.append(binary_list[2])
        del binary_list[2]
        solution = int(str(''.join(binary_list)), 2)

    print(f"{soldier}\t\t\t{solution}")
    soldier += 1
