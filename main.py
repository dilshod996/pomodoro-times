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
timers = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timers)
    timer.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    my_canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_button():
    global reps
    reps+=1

    if reps % 8 == 0:
        count_down(60*LONG_BREAK_MIN)
        change_title("Long Break", PINK)
    elif reps % 2 == 0:
        count_down(60*SHORT_BREAK_MIN)
        change_title("Break", RED)
    else:

        count_down(60 * WORK_MIN)
        change_title("Work", GREEN)
        new_mark = ""
        work_session = math.floor(reps/2)
        for x in range(work_session):
            new_mark += "✔"
        check_mark.config(text=new_mark)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timers
    count_min = math.floor(count/ 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec ==0:
        count_sec ="00"
    if count_min == 0:
        count_min = "00"
    my_canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timers = window.after(1000, count_down, count-1)
    else:
        start_button()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg= YELLOW)

my_canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

my_canvas.create_image(100, 112, image=tomato_img)
timer_text = my_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
my_canvas.grid(row=1, column=1)



timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer.grid(row=0, column=1)

def change_title(textn, color):
    timer.config(text=textn, fg=color, font=(FONT_NAME, 40, "bold"), bg=YELLOW)


star_button = Button(text="Start", command=start_button, highlightthickness=0)
star_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

check_mark = Label(font=(FONT_NAME, 15, "normal"), bg=YELLOW, fg=GREEN)
check_mark.grid(row=3, column=1)
mark = ""






window.mainloop()