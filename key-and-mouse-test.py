import keyboard
import mouse
import time

# recording = keyboard.record(until='esc')
# keyboard.play(recording, speed_factor=1)

# recording = mouse.record() # right click to stop recording
# print("done recording")
# mouse.play(recording)

# time.sleep(30)
# keyboard.write("Hello World")
# print("done typing")

# def test(): 
#     keyboard.write("Hello World")

# keyboard.add_hotkey('q', test)

# while True:
#     pass 

def auto_click(): 
    mouse.click('left')
    # time.sleep(0.1)  # Adjust the delay as needed

keyboard.add_hotkey('q', auto_click)
keyboard.wait('esc')  # Wait for 'esc' to exit the program