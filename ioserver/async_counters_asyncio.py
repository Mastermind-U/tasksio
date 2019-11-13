import random
import asyncio


async def nums():
    while True:
        print(random.random())
        await asyncio.sleep(0.3)


async def constant():
    c = 0
    while True:
        if c % 3 == 0:
            print(random.choice((True, False)))
        c += 1
        await asyncio.sleep(0.3)


async def main():
    await asyncio.gather(
        asyncio.create_task(nums()),
        asyncio.create_task(constant()),
    )


if __name__ == "__main__":
    asyncio.run(main())
