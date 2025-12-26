import multiprocessing
import time

def sq():
    for n in range(1,6):
        time.sleep(1)
        print(n*n)

def cb():
    for n in range(1,6):
        time.sleep(1)
        print(n*n*n)


if __name__ == "__main__":
    
    p1 = multiprocessing.Process(target=sq)
    p2 = multiprocessing.Process(target=cb)

    current = time.time()
    p1.start()
    p2.start()
    # join the 2 threads to the main original thread after completing the process
    p1.join()
    p2.join()

    final = time.time()-current

    print(f"Completed work in time: {final}")