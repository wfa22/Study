print('Введите коэффициенты квадратного уравнения')
a,b,c = map(int,input().split())
d = b**2 - 4*a*c
if d<0:
    print('Корней нет')
else:
    x1=(-b + d**0.5)/(2*a)
    x2=(-b - d**0.5)/(2*a)
    if x1!=x2:
        print(f'Корни уравнения равны {x1}, {x2}')
    else:
        print(f'Корень уравнения равен {x1}')
