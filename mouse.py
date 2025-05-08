import time 
import tkinter as tk
import pynput
from tkinter import messagebox
from tkinter import simpledialog
from pynput import keyboard, mouse
from pynput.mouse import Controller

mouse_movements = [] # List to store mouse movements
start_time = time.time()
root = tk.Tk()
root.title("Mouse Movement Recorder")
root.geometry("300x200")
root.configure(bg="lightblue")
root.withdraw() # Hide the root window
time_set = int(input("Enter runtime please: ")) # amount of time that we are recording mouse movement

def on_move(x, y):
    current_time = time.time()
    if current_time - start_time < time_set: # supposed to be recording
        mouse_movements.append((x, y)) 
    else: 
        return False # stop the listener

with mouse.Listener(on_move=on_move) as listener:
    print("Recording mouse movements for", time_set, "seconds...")
    listener.join() # Start the mouse listener

mouse_controller = Controller()
amt_movements = len(mouse_movements)
print("Recorded", amt_movements, "mouse movements.")
print("while replaying, please dont move your mouse")

# snap mouse to recorded postion that should be playing 
for postion in mouse_movements: 
    mouse_controller.postion = postion
    time.sleep(0.01)
messagebox.showinfo("Mouse Movement Replay", "Mouse movements replayed successfully!")
# root.mainloop()