def dda(x,y,x2,y2):
    dx = abs(x2-x)
    dy = abs(y2-y)
    steps = 0
    if dx>dy:
        steps = dx
    else:
        steps = dy

    increment_x = dx / steps     
    increment_y = dy / steps

    p1 = x
    p3 = y
    x_vars=[p1]
    y_vars=[p3]
    for i in range(steps):
        p1 += increment_x
        n = round(p1)
        x_vars.append(n)

        p3 += increment_y
        n = round(p3)
        y_vars.append(n)
    return x_vars,y_vars


def bresenham(x,y,x2,y2):
    dx = abs(x2 -x)
    dy = abs(y2 -y)
    p = 2 * dy -dx
    x_vars=[]
    y_vars=[]
    while x <= x2:
        x_vars.append(x)
        y_vars.append(y)
        x += 1
        if p<0:
            p = p + 2 * dy
        else:
            p = p + (2 * dy) - (2 * dx)
            y += 1
    return x_vars,y_vars


def puntos_cuadrilateros(x,y):
    return [[1,1],[1,y+1],[x+1,1],[x+1,y+1]]

def puntos_equilateros(b):
    origen = [1,1]
    punto2 = [b,1]
    y = round(((b**2)-((b/2)**2))**0.5)#teorema de pitagoras
    x = round(b/2)
    punto3 = [x,y]
    return[origen,punto2,punto3]


if __name__ == '__main__':
    x = dda(1,1,1,5)
    print (x)