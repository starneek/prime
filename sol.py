# cook your dish here
import random
def isprime(max_a=100):
    a = random.randint(2, max_a)
    problem = a
    if a == 2:
        solution = True
        return (problem, solution)
    if a % 2 == 0:
        solution = False
        return (problem, solution)
    for i in range(3, a // 2 + 1, 2):
        if a % i == 0:
            solution = False
            return (problem, solution)
    solution = True
    return (problem, solution)
print(isprime())
