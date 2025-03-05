from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1/10
SHORT_BREAK_MIN = 1/10
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text= "00:00")
    check_label.config(text="")
    label.config(text="Timer")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_min_sec = WORK_MIN*60
    short_break_min_sec = SHORT_BREAK_MIN * 60
    long_break_min_sec = LONG_BREAK_MIN *60

    if not reps%2 == 0:
        label.config(text="Work Time",fg=GREEN)
        countdown(work_min_sec)
    elif reps%2 ==0:
        label.config(text="Take a short break", fg=PINK)
        countdown(short_break_min_sec)
    elif reps%8 == 0:
        label.config(text="Take a Long break", fg=RED)
        countdown(long_break_min_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_minutes = math.floor(count/60)
    count_seconds = count%60
    if count_seconds > 0 and count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_seconds == 0:
        count_seconds = "00"

    canvas.itemconfig(timer_text,text=f"{count_minutes}:{count_seconds}")
    if count>0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        start_timer()
        mark = ""
        for i in range(math.floor(reps/2)):
            mark+= "✔"
        check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

label = Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
label.grid(column=1,row=0)

check_label = Label(font=(FONT_NAME,8,"bold"),fg=GREEN,bg=YELLOW)
check_label.grid(column=1,row=2)

canvas = Canvas(height=220,width=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,98,image=tomato_img)
timer_text=canvas.create_text(100,120,text="00:00",font=(FONT_NAME,30,"bold"),fill="white")

canvas.grid(column=1,row=1)

start_button=Button(text="Start",width=5,highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",width=5,highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

window.mainloop()

