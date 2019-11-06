
f = lambda x,n: x**3 % n

import asyncio

async def hack():
    n = 7870
    while True:
        for x in range(10000):
            if f(x, n) == 5713 and f(x + 1, n) == 5783:
                for y in range(10000):
                    if f(y, n) == 7821 and f(y + 1, n) == 7870:
                        print('x:{}, y:{}, n:{}, success'.format(x,y,n))
                        return
        n+=1

async def main():
    task = asyncio.create_task(hack())
    await task
    # loop = asyncio.get_event_loop()
    # tasks = [asyncio.ensure_future(hack())]
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()


if __name__ == '__main__':
    asyncio.run(main())