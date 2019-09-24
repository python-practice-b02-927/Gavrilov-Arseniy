import graphics as gr

win = gr.GraphWin("SEMYA", 1000, 1000)

def draw_background(win):
    sky=gr.Rectangle(gr.Point(0,0), gr.Point(1000,500))
    earth=gr.Rectangle(gr.Point(0,1000), gr.Point(1000,500))
    sky.setFill('blue')
    earth.setFill('brown')
    sky.draw(win)
    earth.draw(win)
    
def draw_man(win):
    head=gr.Circle(gr.Point(500, 300), 70)
    body=gr.Circle(gr.Point(500, 500), 130)
    left_arm=gr.Line(gr.Point(370,500), gr.Point(270,600))
    right_arm=gr.Line(gr.Point(630,500), gr.Point(730,600))
    left_leg=gr.Line(gr.Point(500,630), gr.Point(400,730))
    right_leg=gr.Line(gr.Point(500,630), gr.Point(600,730))
    head.setFill('pink')
    body.setFill('green')
    head.draw(win)
    body.draw(win)
    left_arm.draw(win)
    right_arm.draw(win)
    left_leg.draw(win)
    right_leg.draw(win)

def draw_icecream(win):
    
    line1=gr.Line(gr.Point(270,600), gr.Point(220,650))
    line2=gr.Line(gr.Point(220,650), gr.Point(250,670))
    line3=gr.Line(gr.Point(250,670), gr.Point(270,600))
    
    
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    
    

def main(win):
    draw_background(win)
    draw_man(win)
    draw_icecream(win)

    




main(win)

win.getMouse()

win.close()
