import random
import asyncio

async def myCoroutine(id):
    process_time = random.randint(1,5)
    await asyncio.sleep(process_time)
    print("Coroutine: {}, has successfully completed after {} seconds".format(id, process_time))

async def main():
    tasks = []
    for i in range(10):
        # use of ensure_future
        # tasks.append(asyncio.ensure_future(myCoroutine(i)))
        
        # loop.create_task can also be used
        tasks.append(loop.create_task(myCoroutine(i)))

    await asyncio.gather(*tasks)

    # shorter form
    # await asyncio.gather(*[myCoroutine(i) for i in range(10)])


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()