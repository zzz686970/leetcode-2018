# coding:utf-8
# '''Queue
#     Queue.qsize() 返回队列的大小
#     Queue.empty() 如果队列为空，返回True,反之False
#     Queue.full() 如果队列满了，返回True,反之False
#     Queue.full 与 maxsize 大小对应
#     Queue.get([block[, timeout]])获取队列，timeout等待时间
#     Queue.get_nowait() 相当Queue.get(False)
#     Queue.put(item) 写入队列，timeout等待时间
#     Queue.put_nowait(item) 相当Queue.put(item, False)
#     Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
#     Queue.join() 实际上意味着等到队列为空，再执行别的操作
# '''
# import queue
# import threading
# import time

# exitFlag = 0

# class myThread (threading.Thread):
#     def __init__(self, threadID, name, q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.q = q
#     def run(self):
#         print ("开启线程：" + self.name)
#         process_data(self.name, self.q)
#         print ("退出线程：" + self.name)

# def process_data(threadName, q):
#     while not exitFlag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data = q.get()
#             queueLock.release()
#             print ("%s processing %s" % (threadName, data))
#         else:
#             queueLock.release()
#         time.sleep(1)

# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue = queue.Queue(10)
# threads = []
# threadID = 1

# # 创建新线程
# for tName in threadList:
#     thread = myThread(threadID, tName, workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID += 1

# # 填充队列
# queueLock.acquire()
# for word in nameList:
#     workQueue.put(word)
# queueLock.release()

# # 等待队列清空
# while not workQueue.empty():
#     pass

# # 通知线程是时候退出
# exitFlag = 1

# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("退出主线程")

import threading
import time

def run(n):
    ## （mutex）
    lock.acquire()
    global num
    num += 1
    lock.release()

num = 0
lock = threading.Lock()     #实例化一个锁对象
t_obj = [] 

for i in range(20000):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()
    t_obj.append(t)

for t in t_obj:
    t.join()

print ("num:", num)