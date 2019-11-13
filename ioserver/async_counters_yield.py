import random
from time import sleep


def nums():
    while True:
        print(random.random())
        yield


def constant():
    c = 0
    while True:
        if c % 3 == 0:
            print(random.choice((True, False)))
        c += 1
        yield


def main():
    tasks = []
    tasks.append(nums())
    tasks.append(constant())

    while True:
        sleep(0.3)
        task = tasks.pop(0)
        next(task)
        tasks.append(task)


if __name__ == "__main__":
    main()
