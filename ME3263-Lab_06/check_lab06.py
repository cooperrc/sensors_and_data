import numpy as np
def check_p01(Tf_model):
    Tf=np.array([20.00,22.30,23.96,25.14,26.00,26.61,27.06,27.37,27.60,27.77])
    SSE=np.sum((Tf-Tf_model)**2)
    if SSE<=0.01:
        print('Nice work')
        return 3
    else:
        print('Whoops, try again')
        return 0