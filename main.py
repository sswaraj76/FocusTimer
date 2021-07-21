from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_s = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global reps
    window.after_cancel(timer_s)
    canvas.itemconfig(timer, text="00:00")
    label1.config(text="Timer", fg=GREEN)
    label2.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start():
    global reps
    work_sec = WORK_MIN * 60
    short_rest = SHORT_BREAK_MIN * 60
    long_rest = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 2 != 0:
        label1.config(text="Work")
        count_down(work_sec)
    elif reps == 8:
        label1.config(text="Long Break", fg=RED)
        count_down(long_rest)
    elif reps % 2 == 0:
        label1.config(text="Short Break", fg=PINK)
        count_down(short_rest)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer_s
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer_s = window.after(1000, count_down, count - 1)
    else:
        start()
        marks = ""
        work_se = math.floor(reps/2)
        for _ in range(work_se):
            marks += "✔"
            label2.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button1 = Button(text="Start", highlightthickness=0, command=start)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", command=reset)
button2.grid(column=2, row=2)

label1 = Label(text="Time", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label1.grid(column=1, row=0)

label2 = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
label2.grid(column=1, row=3)

window.mainloop()
