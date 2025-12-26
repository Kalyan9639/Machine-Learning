import threading
import time

def num_print():
    for n in range(1,6):
        time.sleep(1)
        print(n)

def al_print():
    for n in ['a','b','c','d','e']:
        time.sleep(1)
        print(n)


if __name__ == "__main__":
    t1 = threading.Thread(target=num_print)
    t2 = threading.Thread(target=al_print)

    current = time.time()
    t1.start()
    t2.start()
    # join the 2 threads to the main original thread after completing the process
    t1.join()
    t2.join()

    final = time.time()-current

    print(f"Completed work in time: {final}")