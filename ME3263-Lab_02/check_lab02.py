import numpy as np

def check_p01(w300,k300,e300):
    if (w300-0.021)/0.021<0.01 and (k300-0.00018)/0.00018<0.01 and (e300-0.0009)/0.0009<0.01:
        points = 2
        print('Nice work!')
        return points
    else:
        points = 0
        print('Whoops, try again')
        return points

def check_p02(x_max_defl,x_max_curv,x_max_strain):
    check = np.isclose([400,0,0],
        np.array([x_max_defl,x_max_curv,x_max_strain]))
    total = np.sum(check)
    if total == 3:
        points = 2
        print('Nice work!')
        return points
    else:
        points = 0
        print('Whoops, try again')
        return points

def check_p03(E31):
    error = (E31-70.2)/70.2
    total = np.isclose(error,-0.09,atol=0.01)
    if total == 3:
        points = 2
        print('Nice work!')
        return points
    else:
        points = 0
        print('Whoops, try again')
        return points
        