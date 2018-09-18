import os
from multiprocessing import Process, Pool, Queue
import time
import random
import _thread
import threading
import queue

def print_time(threadName, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print("%s: %s" %(threadName, time.ctime(time.time())))

def test1():
	try:
		_thread.start_new_thread(print_time, ("Thread-1", 2,))
		_thread.start_new_thread(print_time, ("Thread-2", 4,))
	except:
		print("Error")

	while 1:
		pass

exitFlag = 0

threadLock = threading.Lock()
threads = []

class myThread(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print("start: " + self.name)
		threadLock.acquire()
		print_time(self.name, self.counter, 5)
		print("exit: "+ self.name)
		threadLock.release()

def print_time(threadName, delay, counter):
	while counter:
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print("%s: %s" %(threadName, time.ctime(time.time())))
		counter -= 1

def test2():
	# 创建新线程
	thread1 = myThread(1, "Thread-1", 1)
	thread2 = myThread(2, "Thread-2", 2)

	# 开启新线程
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()
	print ("退出主线程")


def test3():

	thread1 = myThread(1, "Thread-1", 1)
	thread2 = myThread(2, "Thread-2", 2)
	thread1.start()
	thread2.start()
	threads.append(thread1)
	threads.append(thread2)

	for t in threads:
		t.join()

	print ("退出主线程")



if __name__ == '__main__':
	# test1()
	# test2()
	test3()


"""threading
threading.currentThread(): 当前线程变量
threading.enumerate(): 返回正在运行指线程list，启动后、结束前，不包括启动前和终止后的线程。
threading.activeCount(): 返回正在运行的线程数量

run(): 用以表示线程活动的方法。
start():启动线程活动。
join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
isAlive(): 返回线程是否活动的。
getName(): 返回线程名。
setName(): 设置线程名。
"""




# print("Process (%s) start..." % os.getpid())

# pid = os.fork()

# ## 子进程永远返回0，父进程返回子进程的id
# if pid == 0:
# 	print("child process: %s, parent process: %s" %(os.getpid(), os.getppid()))
# else:
# 	print("I (%s), create a child process: (%s)" %(os.getpid(), pid))

# def write(q):
# 	for value in ['a','b','c','d']:
# 		print('Put {} in queue'.format(value))
# 		q.put(value)
# 		time.sleep(random.random())

# def read(q):
# 	while True:
# 		value = q.get(True)
# 		print('Get {} from queue'.format(value))

# def long_time_task(name):
# 	print("Run task {} ({})".format(name, os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random() * 3)
# 	end = time.time()
# 	print("Task {} runs {:.2f} seconds".format(name, end-start))

# def run_proc(name):
# 	print('Run child process {}({})'.format(name, os.getpid()))

# if __name__ == '__main__':
# 	# print("Process (%s) start..." % os.getpid())
# 	# p = Process(target = run_proc, args = ('test',))

# 	## 默认4个进程
# 	p = Pool()
# 	for i in range(5):
# 		p.apply_async(long_time_task, args = (i, ))

# 	print("Wait for all subprocesses done")
# 	# p.start()
# 	## 等待子进程结束后再继续往下运行，通常用于进程间的同步
# 	p.close()
# 	p.join()
# 	print("Process end")


# 	## 3
# 	q = Queue()
# 	pw = Process(target=write, args=(q, ))
# 	pr = Process(target=read, args=(q,))

# 	pw.start()
# 	pr.start()
# 	pw.join()
# 	pr.terminate()
