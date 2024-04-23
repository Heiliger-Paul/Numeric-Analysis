def newtonsmethod(func, funcderiv, x, n):

    def f(x):
        f = eval(func)
        return f
    
    def df(x):
        df = eval(funcderiv)
        return df
    
    for intercept in range (1, n):
        i = x - (f(x)/df(x))
        x = i
    print(f"The root was found to be at {x} after {n} iterations")

newtonsmethod("x**2 - 2", "2*x", 2, 10)