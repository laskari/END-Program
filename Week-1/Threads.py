from threading import *
from time import sleep
class Hello(Thread):

    def run(self):
        for i in range(50):
            print("Hello")
            sleep(1)

class Hi(Thread):

    def run(self):
        for i in range(50):
            print("Hi")
            sleep(1)

ob1 = Hello()
ob2 = Hi()

ob1.start()
sleep(0.2)
ob2.start()