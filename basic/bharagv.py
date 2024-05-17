def f1(func):
    def f2():
        print('start')
        func()
        print('end')
    return f2
@f1
def f3():
    print('hello')
    return 4

d=f3()
print(d)