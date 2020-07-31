from threading import Barrier 

## first thread can print before reaching the first barrier
class Foo:
    def __init__(self):
        self.first_barrier = Barrier(2)
        self.second_barrier = Barrier(2)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_barrier.wait()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.first_barrier.wait()
        printSecond()
        self.second_barrier.wait()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.second_barrier.wait()
        printThird()


class Foo:
    def __init__(self):
        self.called = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        while self.called != 0:
            continue
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.called = 1



    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.called != 1:
            continue 
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.called = 2



    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.called != 2:
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.called = 3

from threading import Lock 
# First thread unlocks the first lock that the second thread is waiting on. Second thread unlocks the second lock that the third thread is waiting on.
class Foo:
    def __init__(self):
        self.locks = (Lock(), Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.locks[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.locks[0]:
            printSecond()
            self.locks[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.locks[1]:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()


from threading import Event
# Set events from first and second threads when they are done. Have the second thread wait for first one to set its event. Have the third thread wait on the second thread to raise its event.

class Foo:
    def __init__(self):
        self.done = (Event(), Event())

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.done[0].set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.done[0].wait()
        printSecond()
        self.done[1].set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.done[1].wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


# Start with two closed gates represented by 0-value semaphores. Second and third thread are waiting behind these gates. When the first thread prints, it opens the gate for the second thread. When the second thread prints, it opens the gate for the third thread.
from threading import Semaphore 
class Foo:
    def __init__(self):
        self.gates = (Semaphore(0), Semaphore(0))

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.gates[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.gates[0]
            printSecond()
            self.gates[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.gates[1]:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()


# Have all three threads attempt to acquire an RLock via Condition. The first thread can always acquire a lock, while the other two have to wait for the order to be set to the right value. First thread sets the order after printing which signals for the second thread to run. Second thread does the same for the third.
from threading import Condition 
class Foo:
    def __init__(self):
        self.exec_condition = Condition()
        self.order = 0
        self.first_finish = lambda: self.order == 1
        self.second_finish = lambda: self.order == 2

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        with self.exec_condition:
            printFirst()
            self.order = 1
            self.exec_condition.notify(2)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.exec_condition:
            self.exec_condition.wait_for(self.first_finish)
            printSecond()
            self.order = 2
            self.exec_condition.notify()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.exec_condition:
            # printThird() outputs "third". Do not change or remove this line.
            self.exec_condition.wait_for(self.second_finish)
            printThird()