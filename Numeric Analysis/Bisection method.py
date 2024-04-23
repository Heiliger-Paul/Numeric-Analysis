def Bisection_method(func, a, b, error_accept):
    
    def f(x):
        f = eval(func)
        return f
    

    error = abs(b -a)

    while error > error_accept:
        c = (b+a)/2

        if f(a) * f(b) >=0:
            print("No root found!!!")
            quit()

        elif f(c) * f(a) < 0:
            b = c
            error = abs(b - a)

        elif f(c) * f(b) < 0:
            a = c
            error = abs(b - a)

        else:
            print("something went wrong")
            quit()
    
    print(f"The error is {error}")
    print(f"The lower boundary, a, is {a} and the upper boundary, b, is {b}")


Bisection_method("(4*x ** 3) + 3*x - 3", 0, 1, 0.05)