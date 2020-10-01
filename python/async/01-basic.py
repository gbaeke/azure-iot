import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

# main coroutine; asyncio.run will run this
# async def makes it a coroutine
# in older code you can still see the @asyncio.coroutine decorator
async def main():
    # use of await to suspend execution of main() until finished
    # you cannot use await outside an async def coroutine
    await asyncio.gather(count(), count(), count())



if __name__ == "__main__":
    import time
    s = time.perf_counter()

    # this will not work below Python 3.7
    asyncio.run(main())
    
    # Note: in Python 3.6 you would use the event loop directly
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(main())
    #loop.close()
    
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

    