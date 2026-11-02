from threading import Lock as lock

class Foo:
    def __init__(self):
        self.lock = (lock(), lock())
        self.lock[0].acquire()
        self.lock[1].acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock[0].release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.lock[0]:
          printSecond()
        self.lock[1].release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.lock[1]:
          printThird()