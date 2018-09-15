# imports
import Tkinter as tk
import ttk

from subprocess import call

win = tk.Tk()
win.title("AGC04 Control Panel")
#win.resizable(0, 0) # disable resizing the GUI

# Adding a Label
ledOnLabel = ttk.Label(win, text="LED ON")
ledOnLabel.grid(column=0, row=0)

def led_on():
    #action.configure(text="** LED is ON **")
    ledOnLabel.configure(foreground='red')
    s = call(["rosservice", "call", "/agc04/iocon_srv", "input: '1'"])

def led_off():
    #action.configure(text="** LED is OFF **")
    ledOnLabel.configure(foreground='black')
    s = call(["rosservice", "call", "/agc04/iocon_srv", "input: '0'"])

# Adding a button
action = ttk.Button(win, text="LED ON", command=led_on)
action.grid(column=1, row=0)

action = ttk.Button(win, text="LED OFF", command=led_off)
action.grid(column=1, row=1)

win.mainloop()