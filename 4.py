import turtle as t
def draw(k, order, size):
    if order == 0:
        t.forward(size)
    else:
        draw(k, order-1, size/2)
        t.left(90)
        draw(k, order-1, size/2)
        t.right(90)
        draw(k, order-1, size/2)
        t.right(90)
        draw(k, order-1, size)
        t.left(90)
        draw(k, order - 1, size / 2)
        t.left(90)
        draw(k, order - 1, size / 2)
        t.right(90)
        draw(k, order - 1, size / 2)



draw(400, 5, 200)
