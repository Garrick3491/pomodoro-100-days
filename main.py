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
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    # while reps < 8:
    reps += 1
    if reps % 8 == 0:
        label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps
    minutes = math.floor(count / 60)

    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        marks = ""
        sessions = math.floor(reps / 2)
        for _ in range(sessions):
            marks += "✔"

        checkmarks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
label = Label(text="Timer", font=(FONT_NAME, 50, 'bold'), bg=YELLOW, fg=GREEN)
checkmarks = Label(text="", font=(FONT_NAME, 25, 'bold'), bg=YELLOW, fg=GREEN)

label.grid(column=1, row=0)

checkmarks.grid(column=1, row=3)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start, highlightthickness=0)
reset = Button(text="Reset", command=reset, highlightthickness=0)
start_button.grid(column=0, row=2)

reset.grid(column=2, row=2)

window.mainloop()