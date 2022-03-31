import turtle

pene = turtle.Turtle()

pene.shape('turtle')
def draw(x, f, r):
    for i in range(x):
        pene.forward(f)
        pene.right(r)

draw(200, 100, 179) 
