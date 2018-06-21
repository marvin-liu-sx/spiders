# _*_coding:utf-8_*_
# Time : 2018/6/20 18:29
# User : yy-zhangcong2
# Email: zhangcong2@yy.com
# Python: 3.6.4

"""Documentation comments"""
from multiprocessing import Process, Queue
import threading
import time

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def evaluate_item(x):
    result_item = count(x)
    return result_item


def count(number):
    for i in range(1000):
        time.sleep(0.0001)
        i += 1
    return i * number


lock = threading.Lock()


def run(info_list, n):
    lock.acquire()
    info_list.append(n)
    lock.release()
    print('%s\n' % info_list)


def write(q):
    for i in ['A', 'B', 'C', 'D', 'E', 'F']:
        print('put %s to queue' % i)
        q.put(i)
        time.sleep(0.5)


def read(q):
    while True:
        v = q.get(True)
        print('get %s from queue' % v)


if __name__ == '__main__':
    # from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
    # import time
    # # 串行执行
    # start_time = time.time()
    # for item in arr:
    #     print(evaluate_item(item))
    # print("Sequential execution in " + str(time.time() - start_time), "seconds")
    #
    # # 多线程
    # start_time_1 = time.time()
    # with ThreadPoolExecutor(max_workers=len(arr))as executor:
    #     futures = [executor.submit(evaluate_item, item)for item in arr]
    #     for future in as_completed(futures):
    #         print(future.result())
    # print("Thread pool execution in " + str(time.time() - start_time_1), "seconds")
    # # 多进程
    # start_time_2 = time.time()
    # with ProcessPoolExecutor(max_workers=len(arr))as executor:
    #     futures = [executor.submit(evaluate_item, item) for item in arr]
    #     for future in as_completed(futures):
    #         print(future.result())
    # print("Process pool execution in " + str(time.time() - start_time_2), "seconds")
    # 如果要执行的任务的耗时时间还没有起进程的时间长，则多线程的执行时间是要比多进程的时间快的

    # **********************************************************************************************************************

    #info = []
    # 进程间的内存无法共享
    # for i in range(10):
    #     p = Process(target=run, args=[info, i])
    #     p.start()
    # time.sleep(1)
    # print('------------------threading-------------------')
    # 线程间的内存可以共享
    # for i in range(10):
    #     p = threading.Thread(target=run, args=[info, i])
    #     p.start()

    # **********************************************************************************************************************
    # 进程间通信，利用Queue,Queue是进程安全的队列
    # q = Queue()
    # pw = Process(target=write, args=(q,))
    # pr = Process(target=read, args=(q,))
    # pw.start()
    # pr.start()
    # pr.join()
    # pr.terminate()
    pass
