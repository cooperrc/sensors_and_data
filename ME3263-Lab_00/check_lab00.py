import numpy as np
from scipy.stats import norm, t

def check_p01(data):
    mu=np.mean(data)
    std=np.std(data)
    
    if np.abs(mu-10)/10<0.01 and np.abs(std-1)<0.15 and len(data)==100:
        print('Nice work')
        points=2
        return points
    else:
        print('Whoops, try again')
        points=0
        return points
    
def check_p02(mu,conf_interval):
    if np.abs(mu-10)/10<0.01 and np.abs(conf_interval-0.2)/0.2<0.1:
        points=2
        print('Nice work')
        return points
    else:
        points=0
        print('Whoops, try again')
        return points
    
def check_p03(data1,data2):
    N1=len(data1)
    N2=len(data2)
    mu1=np.mean(data1); mu2=np.mean(data2)
    sigma1=np.std(data1); sigma2=np.std(data2); 

    A=np.abs(N1+N2)/(N1*N2*1.0)
    B=((N1-1)*sigma1**2+(N2-1)*sigma2**2)/(N1+N2-2)

    tstat=np.abs(mu1-mu2)/np.sqrt(A*B)

    print('t=%1.2f'%tstat)

    df=N1+N2-2
    if tstat>t.interval(0.95, df)[1] and (mu1-mu2)/mu1<0.1:
        points=2
        print('Nice work')
        return points
    else:
        print('Whoops, try again')
        return points
    
if __name__=='__main__':
    print('This is the library to check Lab 00 prework')
