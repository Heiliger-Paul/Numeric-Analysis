def fp_method(func, a, b, error_accept):

    def f(x):
        f = eval(func)
        return f
    
    i = 0
    c_before = 0
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    error = abs (c - c_before)

    while error > error_accept:

        c_after = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if f(a) * f(b) >=0:
            print("NO result found")
            quit()

        elif f(c_after) * f(a) < 0:
            error = abs(c_after - b)
            b = c_after
            i = i + 1

        elif f(c_after) * f(b) < 0:
            error = abs(c_after - a)
            a = c_after
            i = i + 1
        
        else:
            print("something went wrong")
            quit()

    print(f"The error remaining is {error}, after {i} iterations")
    print(f"The root can be approximatly found at {c_after}")
    print(f"The lower root boundary, a, is {a}, and the upper root boundary, b, is {b}")


fp_method("(4*x ** 3) + 3*x - 3", 0, 1, 0.05)