from collections import deque
import time
import random
CAPACITY = 10    # 最大存储量
quantity = 0     # 当前存储量


class Scheduler:
    def __init__(self):
        self.actors = {'producers': [],            # 生产者列表
                       'consumers': []}           # 消费者列表
        self.messages = deque()                     # 消息队列

    def add_producer(self, producer):               # 添加生产者
        self.actors['producers'].append(producer)

    def add_consumer(self, consumer):               # 添加消费者
        self.actors['consumers'].append(consumer)

    def send_message(self, actor_type):             # 发送消息
        self.messages.append(actor_type)

    def run(self):
        # 预激活生产者和消费者
        for actor in self.actors['producers'] + self.actors['consumers']:
            next(actor)
        while True:
            if self.messages:
                # 从消息队列中取出一个消息
                actor_type = self.messages.popleft()
                # 随机选择一个生产者消息者
                obj = random.choice(self.actors[actor_type])
                obj.send('')                        # 发送消息
            time.sleep(0.1)


def consumer(num, name, scheduler):                 # 消费者协程
    global quantity
    while True:
        if quantity - num > 0:
            quantity -= num
            print(f'当前储量：{quantity:<5} {name:<5} 消费 {num} 个产品')
            scheduler.send_message('consumers')
            print(f'当前储量：{quantity:<5} {name:<5} 发消息给 消费者')
            yield
        else:
            scheduler.send_message('producers')
            print(f'当前储量：{quantity:<5} {name:<5} 发消息给 生产者')
            yield


def producer(num, name, scheduler):                 # 生产者协程
    global quantity
    while True:
        yield
        quantity += num
        if quantity > CAPACITY:
            quantity = CAPACITY
        print(f'当前储量：{quantity:<5} {name:<5} 补充库存')
        scheduler.send_message('consumers')


if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.add_producer(producer(5, 'p1', scheduler))
    scheduler.add_producer(producer(4, 'p2', scheduler))
    scheduler.add_consumer(consumer(2, 'c1', scheduler))
    scheduler.add_consumer(consumer(3, 'c2', scheduler))

    scheduler.run()
