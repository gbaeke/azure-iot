# Note: samples make use of asyncio in Python

These examples were tested on Python 3.6. You will often find samples that require Python 3.7 or higher. There are some subtle changes.

For instance:

- Python 3.7: ayncio.create_task() top-level function
- Python 3.6: create_task() is a method on the event loop

So in Python 3.6 (also works in higher versions):

loop = asyncio.get_event_loop()
loop.create_task(some_coroutine)