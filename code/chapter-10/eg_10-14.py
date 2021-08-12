import asyncio
from asyncio import start_server
from datetime import datetime


async def service_task(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f'客户端{addr}连接成功，等待输入 ...')
    while True:
        data_recv = await reader.read(1024)    # 异步接收数据
        data_recv = data_recv.decode('utf-8')
        now = datetime.now().strftime("%H:%M:%S")
        print(f'{now} 接收到来自{addr}的数据：{data_recv}')
        send_data = f'接收到长度为 {len(data_recv)} 的数据'
        writer.write(send_data.encode('utf-8'))
        await writer.drain()                   # 等待缓冲区刷新
        if data_recv == '':
            break
    writer.close()                             # 关闭输出流
    print(f'客户端{addr}连接结束！')


async def main():
    server = await start_server(service_task,  # 创建服务器对象
                                '127.0.0.1', 9000)
    print('TCP服务器启动，监听之中... ...')
    async with server:
        await server.serve_forever()           # 运行服务器

if __name__ == '__main__':
    asyncio.run(main())
