import turtle as t
def draw(k, order, size):
    if order == 0:
        t.forward(size)
    else:
        draw(k, order-1, size/3)
        t.left(60)
        draw(k, order-1, size/3)
        t.right(120)
        draw(k, order-1, size/3)
        t.left(60)
        draw(k, order-1, size/3)
draw(400, 5, 2000)