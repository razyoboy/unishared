import numpy as np
import decimal
#fuckyou
def func(x):
    return np.exp(-x/4)*(2-x)-1

def secant(func, XL, XR, tol):
    fL = func(XL)
    fR = func(XR)
    if fL*fR >= 0:
        print("nno")

    root = (((XL*fR) - (XR*fL)) / (fR - fL))
    funcroot = func(root)

    while abs(funcroot) > tol:
        if fL * funcroot >= 0:
            XL = root
            fL = funcroot
        else: XR = root

        root = (((XL*fR) - (XR*fL)) / (fR - fL))
        funcroot = func(root)
    else: return root

res = secant(func, -2,2,0.00000001); print(res)