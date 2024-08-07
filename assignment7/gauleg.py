import math

def f(x):
    return x*math.exp(x)

def gauleg(x1, x2, x, w, n):
    EPS = 3.0e-16
    m = (n + 1) // 2
    xm = 0.50 * (x2 + x1)
    xl = 0.50 * (x2 - x1)
    
    for i in range(1, m + 1):
        z = math.cos(math.pi * (i - 0.25) / (n + 0.50))
        while True:
            p1 = 1.0
            p2 = 0.0
            for j in range(1, n + 1):
                p3 = p2
                p2 = p1
                p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j
            
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            z1 = z
            z = z1 - p1 / pp
            
            if abs(z - z1) > EPS:
                continue
            
            x[i - 1] = xm - xl * z
            x[n - i] = xm + xl * z
            w[i - 1] = 2.0 * xl / ((1.0 - z * z) * pp * pp)
            w[n - i] = w[i - 1]
            break

# Example usage:
# n = 3
# x = [0.0] * n
# w = [0.0] * n
# x1, x2 = -1.0, 1.0
# gauleg(x1, x2, x, w, n)
# print("x =", x)
# print("w =", w)

# sum = 0.0
# for i in range(0,n):
#     sum = sum + w[i]*f(x[i])
# print(f"sum = ",{sum})
# exact = 2/math.exp(1)
# print(f"Relative error =",{abs(sum-exact)/exact})

