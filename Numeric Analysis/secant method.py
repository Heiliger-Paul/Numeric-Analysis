def secantmethod(func, x0, x1, n):

    def f(x):
        f = eval(func)
        return f
    
    for intercept in range(1, n):
        fx0 = f(x0)
        fx1 = f(x1)

        xi = x0 - (fx0 / ((fx0 - fx1) / (x0 - x1)))

        x0 = x1
        x1 = xi

    print(f"The root was found to be at {x1} after {n} iterations")

secantmethod("x**2 -3", 1 , 3, 5)