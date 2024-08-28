from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg= YELLOW, highlightthickness= 0) 

def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        Timer_label.config(text= "Break", fg= RED)
    elif REPS % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        Timer_label.config(text= "Break", fg= PINK)
    else:
        countdown(WORK_MIN * 60)
        Timer_label.config(text= "Work", fg= GREEN)

canvas = Canvas(width=360, height= 360,bg= YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(180, 180, image= tomato_img)
timer_text = canvas.create_text(180, 200, text= "00:00", fill= "black", font= (FONT_NAME, 35, "bold"))
canvas.grid(column= 1, row= 1) 

def cancel_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    Timer_label.config(text= "Timer")
    chekmark_label.config(text= "")
    global REPS
    REPS = 0
def countdown(count):
    count_min = math.floor(count / 60) 
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"  
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        
        timer = window.after(1000, countdown, count - 1)  
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✔"
        chekmark_label.config(text= marks)


Timer_label = Label(text= "Timer", fg= GREEN, bg= YELLOW, font= (FONT_NAME, 30, "bold"))
Timer_label.grid(column= 1, row= 0)

button_start = Button(text= "Start", highlightthickness= 0, command= start_timer)
button_start.grid(column= 0, row= 2)

reset_button = Button(text= "Reset", highlightthickness= 0, command= cancel_timer)
reset_button.grid(column= 2, row= 2)

chekmark_label = Label( fg= GREEN, bg= YELLOW)
chekmark_label.grid(column= 1, row= 3)



window.mainloop()
