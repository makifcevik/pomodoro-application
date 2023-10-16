from tkinter import *
from tkinter.ttk import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global reps

    window.after_cancel(timer)
    label_title.config(text="Timer", foreground=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    label_check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    # LONG BREAK
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label_title.config(text="BREAK", foreground=RED)

    # SHORT BREAK
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label_title.config(text="BREAK", foreground=PINK)

    # WORK
    else:
        count_down(WORK_MIN * 60)
        label_title.config(text="WORK", foreground=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(time):
    global reps, timer

    count_min = time // 60
    count_sec = time % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if time > 0:
        timer = window.after(1000, count_down, time - 1)
    else:
        start_timer()
        marks = ""
        completed_work = int(reps / 2)
        for i in range(completed_work):
            marks += CHECK
            label_check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

canvas = Canvas(width=200, height=224)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.config(bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)


label_title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), foreground=GREEN, background=YELLOW)
label_title.grid(column=1, row=0)

button_start = Button(text="Start")
button_start.grid(column=0, row=2)
button_start.config(command=start_timer)

button_reset = Button(text="Reset", command=reset)
button_reset.grid(column=2, row=2)

label_check = Label(font=(FONT_NAME, 14, "bold"), foreground="green", background=YELLOW)
label_check.grid(column=1, row=3)


window.mainloop()
