import requests
import time
import asyncio

def load_url(url):
    response = requests.get(url)
    return response.text
def sequential_load():
    urls = ["#"] * 100  
    start_time = time.time()

    for url in urls:
        load_url(url)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"последовательно {elapsed_time}")

async def asynchron_load(url):
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, load_url, url)
    response = await future
    return response

async def asynchron_main():
    urls = ["#"] * 100  
    start_time = time.time()

    tasks = []
    for url in urls:
        task = asyncio.ensure_future(asynchron_load(url))
        tasks.append(task)

    responses = await asyncio.gather(*tasks)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"асинхронно {elapsed_time}")

# Вызов функций
sequential_load()
asyncio.run(asynchron_main())

