import functools
import sys
import time


FILENAME = "eng_vocab.txt"


class MyContextManager():
    def __init__(self, filename, operation):
        try:
            self._file = open(filename, operation)
        except FileNotFoundError:
            print("File not found")
            exit()

    def __enter__(self):
        # print("File is opened and fetched")
        return self._file

    def __exit__(self, type, value, traceback):
        # print("Closing File")
        self._file.close()


def time_consume(func):
    @functools.wraps(func)
    def wrap():
        start = time.time()
        func()
        end = time.time()
        period = end - start
        print("Execution time :%0.8f seconds (%s)" % (period, func.__name__))
    return wrap


def my_generator(text_lines):
    for line in text_lines:
        yield line


@time_consume
def read_list():
    with MyContextManager(FILENAME, "r") as file:
        text_list = file.read().splitlines()
        print(sys.getsizeof(text_list), "Bytes are used by the list")


@time_consume
def read_generator():
    with MyContextManager(FILENAME, "r") as file:
        text = file.read().splitlines()
        my_iterator = my_generator(text)
        for item in my_iterator:
            pass
        print(sys.getsizeof(my_iterator), "Bytes are used by the generator")


def main():
    read_list()
    read_generator()


if __name__ == "__main__":
    main()
