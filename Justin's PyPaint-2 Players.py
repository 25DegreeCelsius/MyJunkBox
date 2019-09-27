#Justin's PyPaint for 4 Players
from tkinter import*
#변수 설정
canvas_height=400
canvas_width=600
canvas_color="yellow"

line_width = 5
line_length = 5

p1_x=canvas_width/2
p1_y=canvas_height
p1_color="blue"


p2_x=canvas_width/2
p2_y=canvas_height/2
p2_color="white"

#사용자 컨트롤
def p1_move_N(event):
    global p1_y
    canvas.create_line(p1_x,p1_y,p1_x,(p1_y-line_length),width=line_width,fill=p1_color)
    p1_y=p1_y-line_length

def p1_move_S(event):
    global p1_y
    canvas.create_line(p1_x,p1_y,p1_x,p1_y+line_length,width=line_width,fill=p1_color)
    p1_y=p1_y+line_length

def p1_move_E(event):
    global p1_x
    canvas.create_line(p1_x,p1_y,p1_x+line_length,p1_y,width=line_width,fill=p1_color)
    p1_x=p1_x+line_length

def p1_move_W(event):
    global p1_x
    canvas.create_line(p1_x,p1_y,p1_x-line_length,p1_y,width=line_width,fill=p1_color)
    p1_x=p1_x-line_length

def p2_move_N(event):
    global p2_y
    canvas.create_line(p2_x,p2_y,p2_x,(p2_y-line_length),width=line_width,fill=p2_color)
    p2_y=p2_y-line_length

def p2_move_S(event):
    global p2_y
    canvas.create_line(p2_x,p2_y,p2_x,p2_y+line_length,width=line_width,fill=p2_color)
    p2_y=p2_y+line_length

def p2_move_E(event):
    global p2_x
    canvas.create_line(p2_x,p2_y,p2_x+line_length,p2_y,width=line_width,fill=p2_color)
    p2_x=p2_x+line_length

def p2_move_W(event):
    global p2_x
    canvas.create_line(p1_x,p1_y,p1_x-line_length,p1_y,width=line_width,fill=p2_color)
    p2_x=p2_x-line_length

def erase_all(event):
    canvas.delete(ALL)
# 메인
window=Tk()
window.title("Justin's PyPaint")
canvas=Canvas(bg=canvas_color,height=canvas_height,width=canvas_width,highlightthickness=0)
canvas.pack()

#키보드 컨트롤
window.bind("e",erase_all)
window.bind("<Up>",p1_move_N)
window.bind("<Down>",p1_move_S)
window.bind("<Right>",p1_move_E)
window.bind("<Left>",p1_move_W)
window.bind("w",p2_move_N)
window.bind("s",p2_move_S)
window.bind("d",p2_move_E)
window.bind("a",p2_move_W)



