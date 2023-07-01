
import time
import threading
from workers.SqSumWorker import SqSumWorker
from workers.SleepyWoker import SleepyWorker

def main():
    n = 6
    start_time = time.time()
    current_workers = []
    for i in range(1,n):
        sqsum = SqSumWorker(n=i*9999)
        current_workers.append(sqsum)

    for i in range(len(current_workers)):
        current_workers[i].join()
    print(f"Total time taken in sqsum {round(time.time()-start_time,2)}")

    start_time = time.time()
    current_workers = []
    for sec in range(1, n):
        sleepy = SleepyWorker(n=sec)#, daemon=True)
        current_workers.append(sleepy)
    for i in range(len(current_workers)):
        current_workers[i].join()
    print(f"Total time taken in sleep {round(time.time()-start_time,2)}")

    print("Process Completed")


if __name__ == "__main__":
    main()