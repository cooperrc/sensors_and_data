import numpy as np

def check_p01(Answer):
    if Answer=='no':
        print('Nice work')
        points=2
        return points
    else:
        print('Whoops, try again')
        points=0
        return points
    
def check_p02(tstat,Answer):
    if np.abs(tstat-3.1)/3.1<0.01 and Answer=='yes':
        points=2
        print('Nice work')
        return points
    else:
        points=0
        print('Whoops, try again')
        return points
 
if __name__=='__main__':
    print('This is the library to check Lab 00 prework')