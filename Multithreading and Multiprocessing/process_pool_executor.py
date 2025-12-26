from concurrent.futures import ProcessPoolExecutor
import time

def square(n):
    time.sleep(1)
    return f"square: {n*n}"

n = [1,2,3,4,5,6,7,89,0,2]

if __name__=="__main__":
    current = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square,n)
    final = time.time() - current
    for result in results:
        print(result)
    print("Completed in ",final,"sec")