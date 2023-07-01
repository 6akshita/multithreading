import threading
import time


class SqSumWorker(threading.Thread):

    def __init__(self, n, **kwargs):
        super(SqSumWorker, self).__init__(**kwargs)
        self.n = n
        self.daemon = True
        self.start()

    def _sqsum(self):
        sq = 0
        for i in range(1,self.n):
            sq += i**2
        print(f"Square Sum is {sq}")

    def run(self) -> None:
        self._sqsum()
