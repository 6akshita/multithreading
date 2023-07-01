
import threading
import time

class SleepyWorker(threading.Thread):

    def __init__(self, n, **kwargs):
        super(SleepyWorker, self).__init__(**kwargs)
        self.n = n
        self.start()

    def _sleepy(self):
        time.sleep(self.n)
        print(f"Sleeping for {self.n} time")

    def run(self) -> None:
        self._sleepy()