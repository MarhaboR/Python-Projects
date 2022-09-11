
#amagine y' = -0.5(y+3)
def f(x, y):
    return x - y

def e_method(x0, y0, xn, n):
    h = float(input("step size: "))
    print('x0\ty0\tXn\tyn')
    for i in range(n):
        Xn = f(x0, y0)
        yn = y0 + h * Xn
        print('%.3f\t%.3f\t%0.3f\t%.3f' % (x0, y0, Xn, yn))
        y0 = yn
        x0 = x0 + h

    print('\nAt x=%.4f, y=%.4f' % (xn, yn))

print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Enter calculation point: ')
xn = float(input('xn = '))

step = int(input('Step number: '))

e_method(x0, y0, xn, step)

