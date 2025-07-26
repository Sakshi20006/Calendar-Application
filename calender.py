from tkinter import *
import calendar

def showCalendar():
    try:
        year = int(year_field.get())
        text_area.delete('1.0', END)
        cal = calendar.TextCalendar(calendar.SUNDAY)
        for month in range(1, 13):
            cal_data = cal.formatmonth(year, month)
            text_area.insert(END, f"{cal_data}\n")
    except ValueError:
        text_area.delete('1.0', END)
        text_area.insert('1.0', "Please enter a valid year!")

# Main window
root = Tk()
root.title("Calendar")
root.config(bg="light grey")
root.geometry("600x700")

# Title
title_label = Label(root, text="Calendar", font=("Helvetica", 24, "bold"), bg="light grey")
title_label.pack(pady=10)

# Entry Frame
input_frame = Frame(root, bg="light grey")
input_frame.pack(pady=5)

year_label = Label(input_frame, text="Enter Year:", font=("Arial", 12), bg="light grey")
year_label.grid(row=0, column=0, padx=5)

year_field = Entry(input_frame, width=10, font=("Arial", 12))
year_field.grid(row=0, column=1, padx=5)

show_button = Button(input_frame, text="Show Calendar", font=("Arial", 12), bg="sky blue", command=showCalendar)
show_button.grid(row=0, column=2, padx=10)

# Text area for calendar
# Frame to hold Text widget and Scrollbar
text_frame = Frame(root)
text_frame.pack(pady=10)

# Scrollbar
scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Text area for calendar with vertical scrollbar
text_area = Text(text_frame, width=70, height=30, font=("Consolas", 10), yscrollcommand=scrollbar.set, wrap=NONE)
text_area.pack(side=LEFT, fill=BOTH)

# Link scrollbar and text widget
scrollbar.config(command=text_area.yview)


# Run the app
root.mainloop()
