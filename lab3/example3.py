import graphics as gr

window = gr.GraphWin("Ozero", 1000, 1000)

ozero = gr.Circle(gr.Point(0, 0), 700)
ozero.setFill('blue')

eye1 = gr.Circle(gr.Point(550, 180), 50)
eye2 = gr.Circle(gr.Point(150, 580), 50)
eye1.setFill('green')
eye2.setFill('green')

mouth99 = gr.Line(gr.Point(800, 800), gr.Point(760, 760))
mouth299 = gr.Line(gr.Point(800, 810), gr.Point(760, 770))
mouth399 = gr.Line(gr.Point(800, 820), gr.Point(760, 780))
mouth99.setWidth(5)
mouth99.setOutline('red')
mouth299.setWidth(5)
mouth299.setOutline('red')
mouth399.setWidth(5)
mouth399.setOutline('red')
mouth499 = gr.Line(gr.Point(740,810 ), gr.Point(820, 770))
mouth499.setWidth(5)
mouth499.setOutline('violet')

kreker = gr.Oval(gr.Point(980,980),gr.Point(1000,1000))
kreker.setFill('red')
kreker.draw(window)


















eyebrow1 = gr.Rectangle(gr.Point(100, 100), gr.Point(300, 300))
eyebrow1.setWidth(10)
eyebrow1.setOutline('black')


mouth = gr.Line(gr.Point(150, 260), gr.Point(250, 260))
mouth2 = gr.Line(gr.Point(250, 260), gr.Point(250, 160))
mouth3 = gr.Line(gr.Point(250, 160), gr.Point(150, 260))
mouth.setWidth(20)
mouth.setOutline('black')
mouth2.setWidth(20)
mouth2.setOutline('black')
mouth3.setWidth(20)
mouth3.setOutline('black')

ozero.draw(window)
eye1.draw(window)
eye2.draw(window)

cluch = gr.Circle(gr.Point(1000, 1000), 700)
cluch.setFill('yellow')

eyebrow1.draw(window)
mouth.draw(window)
cluch.draw(window)
mouth2.draw(window)
mouth3.draw(window)
mouth99.draw(window)
mouth399.draw(window)
mouth299.draw(window)
mouth499.draw(window)

message = gr.Text(gr.Point(300,500), "Макарошки с сыром" )
message.setTextColor('orange')
message.setStyle('italic')
message.setSize(20)
message.draw(window)

window.getMouse()

window.close()
