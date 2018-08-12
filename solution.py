def f_c(x):
	return 4
""" Returns the constant 4 for any input parameter. """
print (f_c(3)) # x = 3 is set as an example. 3 can be changed to another number

def f_x(x, a, b):
        f = a*x + b
        return f
print (f_x(3,2,3))

def sum(x):
        s=0
        for i in range(1,4):     
                s += f_x(x, i, i)
        return s
print (sum(3))
