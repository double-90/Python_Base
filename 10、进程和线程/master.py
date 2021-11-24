# -*- coding:utf-8 -*-


from multiprocessing.managers import BaseManager
from multiprocessing.queues import Queue
import queue, random


# 创建队列：任务队列 task_queue  结果队列 result_queue
task_queue = queue.Queue()
result_queue = queue.Queue()

# 自定义管理器
class Queue_manager(BaseManager):
    pass


# 将队列注册到管理器上(序列化不支持匿名函数)
def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


def test():
    Queue_manager.register("task_queue_manager", callable=return_task_queue)
    Queue_manager.register("result_queue_manager", callable=return_result_queue)


    # 连接上远程管理器（设置当前管理器为远程管理器）
    # 注意：在windows系统中你必须要写IP地址，而其他操作系统比如linux操作系统则就不要了
    q = Queue_manager(address=('127.0.0.1', 8001), authkey=b'abc')

    q.start()     # 启动管理器


    task = q.task_queue_manager()
    result = q.result_queue_manager()


    for i in range(10):
        n1 = random.randint(1, 200)
        task.put(n1)
        print(f'{i}: task 队列获取数据 put({n1})')

    print('尝试获得结果')
    for i in range(10):
        try:
            n2 = result.get(timeout=10)
            print(f'{i}: result 队列输出数据 get({n2})')
        except Queue.Empty:
            print('result queue is empty')


    # 关闭管理器
    q.shutdown()
    print('master exit')

 
if __name__ == "__main__":
    test()
