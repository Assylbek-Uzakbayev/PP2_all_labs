def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return (chickens, rabbits)
    return None

print(solve(35, 94))  # Output: (23, 12)
