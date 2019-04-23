import asyncio, random
from asyncio import Future

def gen():
    value = 1
    while True:
        receive = yield value
        value = 'got: %s' % receive


g = gen()
print(g.send(None))
print(g.send('hello'))
print(g.send(123456))

@asyncio.coroutine
def countdown1(n):
    while n > 0:
        print(n)
        n = n - 1

        # 通常yield from后都是接的耗时操作, yield from等于for in yield
        yield from asyncio.sleep(0.3)


print("-----yield from------")
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait([countdown1(5)]))
# loop.close()


async def countdown2(n):
    t = n
    while n > 0:
        print(n)
        # async-await 替代 @asyncio.coroutine 和yield from
        await asyncio.sleep(0.3)
        n -= 1

    return t


async def async_await_test():
    # print(await asyncio.gather(countdown2(3), countdown2(5)))

    # Wait for at most 1 second
    # try:
    #     print(await asyncio.wait_for(countdown2(5), timeout=1.0))
    # except asyncio.TimeoutError:
    #     print("timeout")

    for f in asyncio.as_completed([countdown2(3), countdown2(2), countdown2(1)]):
        print("as_completed:{} all_task:{}".format(await f, len(asyncio.all_tasks())))

    # asyncio.shield(countdown2(3))


async def custom_future_test1():
    r = await fu
    print("custom_future_test1 complete {}".format(r))


async def custom_future_test2():
    await asyncio.sleep(2)
    fu.set_result(666)
    print("custom_future_test2 complete")


print("-----async-await-----")
# asyncio.run(async_await_test())

print("-----custom-future-----")
fu = Future()
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([custom_future_test1(), custom_future_test2()]))
loop.close()

print("end")