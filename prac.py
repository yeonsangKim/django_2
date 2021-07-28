def decorator(func):
    def decorated(a,b):
        try :
            if a>0 and b>0:
                func(a,b)



        except:
            print('error')

    return decorated

@decorator
def tri(a,b):
    x=a*b/2
    print(x)
@decorator
def reg(a,b):
    x=a*b
    print(x)


tri(1,3)
reg(1,3)
