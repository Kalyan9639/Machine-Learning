'''
Real world use case: Factorial of larger numbers CPU - bound tasks
Multiprocessing distributes the workload among the multiple cpu cores
'''

import multiprocessing
import math
import sys
import time

# increase the max no. of digits for integer conversion
sys.set_int_max_str_digits(100000000)

# function to compute factorials of given number
def fact(n):
    print(f"Computing factorial of {n}")
    res = math.factorial(n)
    print(f"Factorial of {n} is {res} \n\n\n")
    return res

if __name__ == "__main__":
    n = [5000,6000,7000]

    start_timer = time.time()
    with multiprocessing.Pool() as pool:
        res = pool.map(fact,n)
    total = time.time() - start_timer

    print(f"\n Time taken: {total}")