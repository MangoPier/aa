# 没有理解这一章节
import _thread
import logging
import threading
from time import sleep,ctime
logging.basicConfig(level=logging.INFO)

# 更优方法：threading
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self): # 改写run函数
        self.func(*self.args)


loops = [2,4]
def loop(nloop,nsec):
    logging.info("start loop" + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloop) + " at "+ ctime())


def main():
    logging.info("start all at +" + ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()
# 需要注意的是loop0\loop1两个线程顺序是不确定的

# 原语
# 锁，解决了数据的互斥访问


"""
# 初阶
# 整个执行时间在6秒，要等前面的执行完了，才能执行loop1，如果前面执行时间太长，会阻塞后面的进度
def loop0():
    logging.info("start loop0 at " + ctime())
    sleep(4)
    logging.info("end loop0 at " + ctime())

def loop1():
    logging.info("start loop1 at " + ctime())
    sleep(2)
    logging.info("end loop1 at " + ctime())

def main():
    logging.info("start all at +" + ctime())
    loop0()
    loop1()
    logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()

"""

"""
# 进阶
def loop0():
    logging.info("start loop0 at " + ctime())
    sleep(4)
    logging.info("end loop0 at " + ctime())

def loop1():
    logging.info("start loop1 at " + ctime())
    sleep(2)
    logging.info("end loop1 at " + ctime())

def main():
    logging.info("start all at +" + ctime())
    _thread.start_new_thread(loop0,())
    _thread.start_new_thread(loop1,()) # 这里loop0\loop1会同时执行
    sleep(6)  # 这里让主线程等待6秒
    # 如果没有这一步，那么整个仅仅打印主线程的内容，start all 以及 end all
    # _thread的缺点：_thread对于进程何时退出没有任何控制。当主线程结束时，所有其他线程也都强制结束。不会发出警告或者进行适当的清理。
    # 因而python多线程一般使用较为高级的threading模块，它提供了完整的线程控制机制以及信号量机制。
    logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()
"""

"""
# 再进阶
# 如果不知道loop0以及loop1的执行时间，那么怎么来让主线程等待这两个执行完呢？
# 可以用锁
loops = [2,4]
def loop(nloop,nsec,lock):
    logging.info("start loop" + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloop) + " at "+ ctime())
    lock.release()


def main():
    logging.info("start all at +" + ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))
    for i in nloops:
        while locks[i].locked(): pass
    logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()

"""