import xlrd
import pymssql





def f1():
    print 'hello world'
    f2()

def f2():
    print 'nihao'
    f3()
    pass
def f3():
    pass

if __name__ == '__main__':
    f1()