
import time
import threading

def sqsum(n):
    sq = 0
    for i in range(1,n):
        sq += i**2
    print(f"Square Sum is {sq}")

def sleep(n):
    time.sleep(n)
    print(f"Sleeping for {n} time")

def main():
    n = 6
    start_time = time.time()
    current_threads = []
    for i in range(1,n):
        t = threading.Thread(target=sqsum, args=(i*999999,))
        t.start()
        current_threads.append(t)
    for i in range(len(current_threads)):
        current_threads[i].join()
    print(f"Total time taken in sqsum {round(time.time()-start_time,2)}")

    start_time = time.time()
    current_threads = []
    for sec in range(1, n):
        t = threading.Thread(target=sleep, args=(sec,))
        t.start()
        current_threads.append(t)
    for i in range(len(current_threads)):
        current_threads[i].join()
    print(f"Total time taken in sleep {round(time.time()-start_time,2)}")

    print("Process Completed")


if __name__ == "__main__":
    main()