import tkinter as tk
import calendar

def show_calendar():
    year = int(year_entry.get())
    output.delete('1.0', tk.END)
    cal = calendar.TextCalendar()
    output.insert(tk.END, cal.formatyear(year))

root = tk.Tk()
root.title("400-Year Calendar")

tk.Label(root, text="Enter Year:").pack()
year_entry = tk.Entry(root)
year_entry.pack()

tk.Button(root, text="Show Calendar", command=show_calendar).pack()
output = tk.Text(root, height=20, width=70)
output.pack()

root.mainloop()
