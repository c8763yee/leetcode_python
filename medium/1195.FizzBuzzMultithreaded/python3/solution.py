from threading import Lock
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.done = False
        self.lock = [Lock(),Lock(),Lock(),Lock()]
        for i in range(1, 4):
            self.lock[i].acquire()
    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.lock[1].acquire()
            if self.done:
                break
            printFizz()
            self.lock[0].release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.lock[2].acquire()
            if self.done:
                break
            printBuzz()
            self.lock[0].release()


    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.lock[3].acquire()
            if self.done:
                break
            printFizzBuzz()
            self.lock[0].release()


    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.lock[0].acquire()
            if i % 15 == 0:
                self.lock[3].release()
            elif i % 3 == 0:
                self.lock[1].release()
            elif i % 5 == 0:
                self.lock[2].release()
            else:
                printNumber(i)
                self.lock[0].release()
        
        self.lock[0].acquire()
        self.done = True
        for xi in range(1, 4):
            self.lock[xi].release()
