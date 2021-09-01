import numpy as np

def check_p01(Y):
    return 2

def check_p02(f1,f2,f3):
    e1=np.abs(f1-36)/36.0
    e2=np.abs(f2-224)/224.0
    e3=np.abs(f3-628)/628.0
    if e1<0.05 and e2<0.05 and e3<0.05:
        print('Nice work')
        return 2
    else:
        print('Whoops, try again')
        return 0