import turtle as t
def draw1(k, order, size):
    if order == 0:
        t.forward(size)
    else:
        t.right(45)
        draw1(k, order-1, size/2)
        t.left(90)
        draw2(k, order-1, size/2)
        t.left(45)

def draw2(k, order, size):
    if order == 0:
        t.forward(size)
    else:
        t.right(45)
        draw1(k, order-1, size/2)
        t.right(90)
        draw2(k, order-1, size/2)
        t.left(45)




draw1(400, 8, 2000)