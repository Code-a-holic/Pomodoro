from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT_TITLE = "Pacifico"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark_count = ""
timer = None
def time_formatter(value):
    count_min = math.floor(value / 60)
    count_sec = value % 60
    time_arr = [count_min, count_sec]
    return time_arr
# ---------------------------- TIMER RESET ------------------------------- #
def timer_soft_reset():
    global check_mark_count
    time_arr  = time_formatter(WORK_MIN*60)
    count_sec = time_arr[1]
    count_min = time_arr[0]
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    check_mark_count = ""
    check_marks.config(text=check_mark_count)

def timer_hard_reset():
    global check_mark_count
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    title.config(text="Timer", fg=GREEN)
    check_mark_count = ""
    check_marks.config(text=check_mark_count)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    rep_modulo = reps % 2
    if reps == 15:
        title.config(text="Relax your mind. You've earned it!", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif rep_modulo == 0:
        title.config(text="This is your time to Work!", fg=RED)
        count_down(WORK_MIN*60)
    elif rep_modulo == 1:
        title.config(text="Break", fg=GREEN)
        count_down(SHORT_BREAK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(value):
    global reps
    global check_mark_count
    time_arr = time_formatter(value)
    count_sec = time_arr[1]
    count_min = time_arr[0]
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if value > 0:
        global timer
        timer = window.after(1000, count_down, value-1)
    else:
        if reps % 2 != 0:
            check_mark_count += "✓"
            check_marks.config(text=check_mark_count)
        reps += 1
        if reps <= 15:
            start_timer()
        else:
            reps = 0
            timer_soft_reset()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

title = Label(text="Timer", font=(FONT_TITLE, 50, "bold"), bg=YELLOW, fg=GREEN)
title.grid(column=1, row=0)
title.config(padx=20, pady=10)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="25:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_TITLE, 17), bg=GREEN, fg="white")
start_button.grid(column=0, row=3)
start_button.config(padx=10, command=start_timer)

check_marks = Label(text="", font=(FONT_TITLE, 30, "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=2)

Reset_button = Button(text="Reset", font=(FONT_TITLE, 17), bg=GREEN, fg="white")
Reset_button.grid(column=2, row=3)
Reset_button.config(padx=10, command=timer_hard_reset)

window.mainloop()