from multiprocessing import Process
import os

# print('hello OS')
# print('my pid is', os.getpid())

def foo():
    print('This is foo')
    print('foo pid is', os.getpid())
    print('parent is ', os.getppid())
    
def bar():
    print('This is bar')
    print('bar pid is', os.getpid())
    print('parent is ', os.getppid())

def baz():
    print('This is baz')
    print('baz pid is', os.getpid())
    print('parent is ', os.getppid())

    
if __name__ == '__main__':
    # print('parent process', os.getpid())
    child1 = Process(target=foo).start()
    child2 = Process(target=bar).start()
    child3 = Process(target=baz).start()

    
    