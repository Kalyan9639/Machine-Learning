from concurrent.futures import ThreadPoolExecutor
import time

def print_num(n):
    time.sleep(1)
    return f"number: {n}"

n = [1,2,3,4,5,6]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_num,n)

for result in results:
    print(result)