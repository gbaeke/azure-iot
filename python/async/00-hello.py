import asyncio, time

async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')

asyncio.run(main())

#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())
#loop.close()