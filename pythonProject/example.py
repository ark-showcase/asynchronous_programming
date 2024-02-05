import asyncio


async def task1():
  print('send first e-mail')
  asyncio.create_task(task2())
  await asyncio.sleep(2)
  print('first e-mail reply')

async def task2():
  print('send second e-mail')
  asyncio.create_task(task3())
  await asyncio.sleep(8)
  print('second e-mail reply')

async def task3():
  print('send third e-mail')
  await asyncio.sleep(2)
  print('third e-mail reply')


asyncio.run(task1())