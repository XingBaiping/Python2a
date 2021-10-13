from timeit import timeit
from collections import deque
from simplequeue import SimpleQueue

SIZE = 10000
TIMES = 100


def measure(function):
    time = timeit(function, number=TIMES)
    time_str = f"Execution time: {time/TIMES:.7f} seconds"
    settings = f"(SIZE: {SIZE}, TIMES: {TIMES}, {function.__name__})"
    print(time_str, settings)


def fifo_queue():
    a_queue = SimpleQueue()
    for i in range(SIZE):
        a_queue.append(i)
    while a_queue._tail:
        a_queue.popleft()


def main():
    measure(fifo_queue)


if __name__ == "__main__":
    main()
