a = float(input('A > '))
b = float(input('B > '))
c = float(input('C > '))

def root(a,b,c):
    x1 =  (-b - (b**2 -4*a*c)**0.5)/(2*a)

    x2 =  (-b + (b**2 -4*a*c)**0.5)/(2*a)

    if a != 0:
        s = (b**2)-4*a*c
        if s == 0:
            x = -b/(2*a)
            return x
        elif s > 0:
            x1 = (-b-(s)**0.5)/(2*a)
            x2 = (-b+(s)**0.5)/(2*a)
            return x1, x2
        elif s < 0:
            x = -b/(2*a)
            y = (-s)**0.5/(2*a)
            
            ans1 = (f"{x} - {y}i")
            ans2 = (f"{x} + {y}i")
            return ans1, ans2
    elif a == 0:
        x = -c/b
        return x

res = root(a,b,c)
print(res)




