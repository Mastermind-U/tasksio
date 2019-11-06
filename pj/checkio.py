import time
import random
import asyncio

def sync_run(name):
    random_int = random.randint(50000, 54304231)
    start = time.time()
    for i in range(random_int):
        pass
    end = time.time() - start
    print(f"{name} with {random_int} iterations took {end} s")

def run_sync_run():
    start = time.time()
    for i in range(10):
        name = f"iteration {i}"
        sync_run(name)
    end = time.time() - start
    print(f"Loop took {end} s")

#run_sync_run()


async def async_run(name):
    random_int = random.randint(50000, 54304231)
    start = time.time()
    for i in range(random_int):
        pass
    end = time.time() - start
    msg = f"{name} with {random_int} iterations took {end} s"
    print(msg)
    return msg

def compile_tasks():
    tasks = []
    for i in range(10):
        name = f"Async iteration {i}"
        tasks.append(
            asyncio.ensure_future(async_run(name))
            )
    return tasks

def main():
    start = time.time()

    tasks = compile_tasks()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

    end = time.time() - start
    print(f"Async loop took {end} sec")

if __name__ == '__main__':
    main()