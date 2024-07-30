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
deps = 0

# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global deps
    deps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if deps == 0:
        countdown(work_sec)

    if deps % 8 == 0:
        countdown(long_break_sec)
        timer.config(text="Break", fg=RED)
    elif deps % 2 == 0:
        countdown(short_break_sec)
        timer.config(text="Break", fg=RED)
    else:
        countdown(work_sec)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global deps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"
    elif count_min == 0:
        count_min = "00"
    canvas.itemconfig(time_text_count, text=f"{count_min}:{count_sec}")
    if count_min == 00 and count_sec == 0:
        print("lake")
    if count > 0:
        window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# Create a canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text_count = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Title timer
timer = Label(text="Timer", font=(FONT_NAME, 50, "bold"), highlightthickness=0, bg=YELLOW)
timer.config(fg=GREEN)
timer.grid(column=1, row=0)

# Button start
button_start = Button(text="Start", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start_time)
button_start.grid(column=0, row=3)

# Button reset
button_reset = Button(text="Reset", font=(FONT_NAME, 15, "bold"), highlightthickness=0)
button_reset.grid(column=2, row=3)

# Check
check = Label(text="✔", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
check.grid(column=1, row=4)
window.mainloop()
