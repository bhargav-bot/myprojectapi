
def decorator(func):
    def donotdosum(*args,**kwargs):
        print('start')
        func(*args,**kwargs)

        print('end')
    return donotdosum

@decorator
def add(a,b):
    print("sum value is:"+str(a+b))  
    return a+b

def sub(a,b):
    print("minus value is:"+str(a-b))
    return a-b
sub=decorator(sub)(4,2)
f=sub
print(f)
d=add(1,2)
print(d)


