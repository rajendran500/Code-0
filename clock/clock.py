from tkinter import Label, Tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_clock)

# Create main window
root = Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.resizable(False, False)

# Create label to display time
label = Label(root, font=('Arial', 40, 'bold'), bg='black', fg='white')
label.pack(expand=True)

update_clock()  # Start updating time
root.mainloop()
