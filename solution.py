
def f_c(x):
	"""Returns the constant 4 for any input parameter."""
	return 4
print (f_c(1)) 

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
