import turtlemax as t
c = t.Canvas()
w = t.Windows()
c.creating_canvas("Canvas_1")
w.set_windows_title("嗨嗨嗨")
# c.show_version()
# c.set_canvas_penfill_color("Canvas_1", "black", "skyblue")
w.set_backgroundcolor("white")
c.set_canvassize("Canvas_1", 5)
w.set_screensize(800, 800, 60, 60)
# c.canvas_onfill()

# for i in range(4):
#     c.forward(100)
#     c.canvas_left(90)

# c.canvas_offfill()
# c.creating_square("Canvas_1", x=0, y=0, width=100, height=100, color="black", size=5, fill=True, fill_color="skyblue")
# c.creating_triangle(x=0, y=0, width=100, color="black", size=5, fill=False, fill_color="skyblue")
# c.creating_hexagon("Canvas_1", x1=0, y1=0, x2=100, y2=100, x3=200, y3=200, x4=200, y4=300, x5=100, y5=300, x6=50, y6=200, color="blue", size=5, fill=True, fill_color="green")
c.set_canvas_hide("Canvas_1")


def fill1():
    for i in range(4):
        c.forward("Canvas_1", 10)
        c.canvas_right("Canvas_1", 90)


text = w.creating_text_input("神秘窗口", "给个三连吧！！！")

c.fill("Canvas_1", fill1, "red")
c.run()
