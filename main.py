from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN)
    elif REPS % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec <= 9:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        check = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            check += " ✔"
        checkmark_label.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

# Labels
checkmark_label = Label(bg=YELLOW)
checkmark_label.grid(row=4, column=2)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45, "bold"))
timer_label.grid(row=1, column=2)

# Buttons
start_button = Button(text="Start", command=start)
start_button.config(padx=10, pady=10, bg=YELLOW)

start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", command=reset)
reset_button.config(padx=10, pady=10, bg=YELLOW)
reset_button.grid(row=3, column=3)

window.mainloop()
