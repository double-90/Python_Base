#! -*- coding:utf-8 -*-

from multiprocessing.managers import BaseManager
from multiprocessing.queues import Queue
import time


class Queue_manager(BaseManager):
    pass


# 管理器注册队列（等连接上远程管理器后，就可以使用远程上同名的队列）
Queue_manager.register("task_queue_manager")
Queue_manager.register("result_queue_manager")


# 连接远程管理器
q = Queue_manager(address=('127.0.0.1', 8001), authkey=b'abc')  

q.connect()

task = q.task_queue_manager()
result = q.result_queue_manager()


for i in range(10):
    try:
        n = task.get(timeout=10)                    # 获取任务队列中的数据
        print("run task %d * %d..." % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)                               # 将结果上传给结果队列
    except Queue.Empty:
        print('task queue is empty')

print('worker exit')
