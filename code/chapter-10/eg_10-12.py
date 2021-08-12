import asyncio


async def coroutine(name):
    print(f'协程 {name} 开始运行...')
    await asyncio.sleep(1)                  # 模拟输入/输出
    print(f'协程 {name} 运行结束！')
    return f'协程{name}运行结果'


async def main():
    c_A = coroutine('A')                    # 协程A
    c_B = coroutine('B')                    # 协程B
    c_C = coroutine('C')                    # 协程C
    r = await asyncio.gather(c_A, c_B, c_C)  # 创建并发任务
    return r

r = asyncio.run(main())
print(r)
