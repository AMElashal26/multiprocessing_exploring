#mprocessing.py
import multiprocessing as mp
from multiprocessing import Process

#print(mp.cpu_count())

#def myfunc():
#    print("Hello World")

def lang_func(lang):
    print(lang)


if __name__ == '__main__':
    #proc = Process(target=myfunc)
    #proc.start()
    #proc.join()
    langs = ['C', 'Python', 'java', 'PHP']
    processes = []
    for l in langs:
        proc = Process(target=lang_func, args=(l,))
        processes.append(proc)
        proc.start()
    for p in processes:
        p.join()