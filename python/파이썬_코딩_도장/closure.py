def calc():
    a = 2
    b = 1
    def mul(x):
        return a * x + b
    return mul

def mul_ind(x):
    return 2 * x + 1

c = calc()
print(c)
c(3)