import asyncio

async def fetch_data(n):

    await asyncio.sleep(2)

    return {'data':n}

async def fetch_all_data(n):

    data = []
    task_holder = []
    for i in range(n):
        task_holder.append(None)
        task_holder[-1] = asyncio.create_task(fetch_data(i))

    for i in range(n):
        data.append(await task_holder[i])

    return {'all_data': data}