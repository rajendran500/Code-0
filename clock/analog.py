from tkinter import Tk, Canvas
import time
import math

def update_clock():
    canvas.delete("all")
    draw_clock()
    root.after(1000, update_clock)

def draw_clock():
    canvas.create_oval(50, 50, 250, 250, outline="black", width=4)
    
    for i in range(12):
        angle = math.radians(i * 30)
        x1 = 150 + 90 * math.sin(angle)
        y1 = 150 - 90 * math.cos(angle)
        x2 = 150 + 100 * math.sin(angle)
        y2 = 150 - 100 * math.cos(angle)
        canvas.create_line(x1, y1, x2, y2, width=3)
    
    current_time = time.localtime()
    
    hour_angle = math.radians((current_time.tm_hour % 12) * 30 + current_time.tm_min * 0.5)
    minute_angle = math.radians(current_time.tm_min * 6)
    second_angle = math.radians(current_time.tm_sec * 6)
    
    hour_x = 150 + 50 * math.sin(hour_angle)
    hour_y = 150 - 50 * math.cos(hour_angle)
    minute_x = 150 + 70 * math.sin(minute_angle)
    minute_y = 150 - 70 * math.cos(minute_angle)
    second_x = 150 + 80 * math.sin(second_angle)
    second_y = 150 - 80 * math.cos(second_angle)
    
    canvas.create_line(150, 150, hour_x, hour_y, width=6, fill="black")
    canvas.create_line(150, 150, minute_x, minute_y, width=4, fill="blue")
    canvas.create_line(150, 150, second_x, second_y, width=2, fill="red")
    
    canvas.create_oval(145, 145, 155, 155, fill="black")

root = Tk()
root.title("Analog Clock")
root.geometry("300x300")
canvas = Canvas(root, width=300, height=300, bg="white")
canvas.pack()
update_clock()
root.mainloop()
