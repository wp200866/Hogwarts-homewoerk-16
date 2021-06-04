import _thread
import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)   # 添加日志信息  ，level 日志的输出等级，所有的INFO级别都会进行打印输出

# class方法
loops = [2,4]
class MyTread(threading.Thread):   # 声明一个类，继承threading的Thread类
    def __init__(self, func, args, name=''):   # 构造函数：传递函数，参数，类
        threading.Thread.__init__(self)   # 主动调用方法
        self.func = func     # 存入实例变量中
        self.args = args
        self.name = name

    def run(self):   # 重写 run 方法
        self.func(*self.args)   # 解元组

def loop(nloop, nsec):
    logging.info("start loop " + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop " + str(nloop) + " at " + ctime())

def main():
    logging.info(" start all at " + ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyTread(loop, (i, loops[i]), loop.__name__)   # 调用声明的方法
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()   # join 会去等thread[0]是否结束
    logging.info(" end all at " + ctime())


# # threading方法
# loops = [2,4]
# def loop(nloop, nsec):
#     logging.info("start loop " + str(nloop) + " at " + ctime())
#     sleep(nsec)
#     logging.info("end loop " + str(nloop) + " at " + ctime())
#
# def main():
#     logging.info(" start all at " + ctime())
#     threads = []
#     nloops = range(len(loops))
#
#     for i in nloops:
#         t = threading.Thread(target=loop, args=(i, loops[i]))
#         threads.append(t)
#     for i in nloops:
#         threads[i].start()
#     for i in nloops:
#         threads[i].join()   # join 会去等thread[0]是否结束
#     logging.info(" end all at " + ctime())


# # _thread方法
# loops = [2,4]
# def loop(nloop, nsec, lock):
#     '''
#     :param nloop: 用于标识当前 loop 处于第几个
#     :param nsec: 时间，loop循环多久
#     :param lock: 已经锁上的锁
#     :return:
#     '''
#     logging.info("start loop " + str(nloop) + " at " + ctime())  # nloop
#     sleep(nsec)   # 动态时间
#     logging.info("end loop " + str(nloop) + " at " + ctime())
#     lock.release()   # _thread自动的方法，解锁
#
# def main():
#     logging.info("start all at " + ctime())
#     locks=[]  # 声明一个锁，把每个锁传进来
#     nloops = range(len(loops))   # 处于第几个线程
#     for i in nloops:
#         lock = _thread.allocate_lock()  # 声明一个新的锁
#         lock.acquire()  # 把这个锁锁上
#         locks.append(lock)  # 传递给locks，locks就有了所有的锁
#     for i in nloops:  # 用来启线程
#         _thread.start_new_thread(loop, (i, loops[i], locks[i]))
#     for i in nloops:  # 判断锁是否被释放
#         while locks[i].locked(): pass  # 如果未解锁，会一直循环；如果被解锁，退出死循环
#     logging.info("end all at " + ctime())


# # 主流程演示
# def loop0():
#     logging.info("start loop0 at " + ctime())  # ctime打印当前时间
#     sleep(4)
#     logging.info("end loop0 at " + ctime())
#
# def loop1():
#     logging.info("start loop1 at " + ctime())
#     sleep(2)
#     logging.info("end loop1 at " + ctime())
#
# def main():
#     logging.info("start all at " + ctime())
#     _thread.start_new_thread(loop0,())  # _thread的缺点：当主线程退出时，所有的子线程都会被kill掉
#     _thread.start_new_thread(loop1,())
#     sleep(6)  # 如果不加的话，会导致子线程还未进行，主线程就已经结束了
#     logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()

# 原语
## 锁
## 信号量