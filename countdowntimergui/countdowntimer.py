"""Monolithic Python file to generate a basic countdown timer GUI."""

import tkinter as tk
import tkinter.ttk as ttk
# messagebox has to be explicitly imported from tkinter
from tkinter import messagebox
import time

"""
Classic widgets come from tk, Themed widgets come from ttk submodule.

Themed widgets give a native look and feel for a given operating system.
There are also brand-new widgets, such as the progress bar, weren't
available in Tkinter before. Some of the classic widgets do not have a
themed alternative.

from tkinter import *
from tkinter.ttk import *

Using the wildcard imports in the order above overrides classic widgets
with themed widgets whenever available. Normally I wouldn't use wildcard
imports, but it could make sense to override the Tkinter widgets. I
didn't end up doing this because I prefer the classic widget functionality.
"""

window = tk.Tk()
window.title("Custom Countdown Timer")
window.geometry("650x350")
window.configure(background="grey")

hour, minute, second = tk.StringVar(), tk.StringVar(), tk.StringVar()
hour.set("00")
minute.set("00")
second.set("00")

txt_hour = tk.Entry(window, width=4, font=("Arial", 24), textvariable=hour)
txt_hour.place(x=240, y=100)

txt_minute = tk.Entry(window, width=4, font=("Arial", 24), textvariable=minute)
txt_minute.place(x=300, y=100)

txt_second = tk.Entry(window, width=4, font=("Arial", 24), textvariable=second)
txt_second.place(x=360, y=100)


def start_button_command() -> None:
	"""Start the countdown timer."""
	print('start button clicked')
	try:
		# convert time to seconds for countdown
		num_of_seconds = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())

		# calculate increment for the progress bar
		prog_increment = 100 / num_of_seconds
	except ValueError:
		print("Input a valid value")
		tk.messagebox.showinfo("Countdown Timer", "Input a valid value")

	while num_of_seconds > -1:
		mins, secs = divmod(num_of_seconds, 60)
		hours = 0
		if mins > 60:
			hours, mins = divmod(mins, 60)

		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

		window.update()
		time.sleep(1)

		if num_of_seconds == 0:
			# TODO: can't get sound to play and messagebox to pop up
			# window.bell()
			tk.messagebox.showinfo("Countdown Timer", "Time's up")

		num_of_seconds -= 1
		prog['value'] += prog_increment


def stop_button_command() -> None:
	"""Stop the countdown timer."""
	print('stop button clicked')


label = tk.Label(
	text="Countdown Timer",
    foreground="white",  # Set the text color to white
    background="#3EC1D3",  # Set the background color to Hex color code (light blue)
    font=("Arial", 30),
    width=15,
    height=2
    ).pack()

"""
TODO: fix layout of buttons, they're not quite centered.
Also consider placing them relative to the window size, 
rather than hard-coding the placement.
"""
btn_start = tk.Button(
	text="Start Countdown",
	command=start_button_command,
	cursor="gumby",
	height=2,
	width=10
	)

btn_start.pack()
btn_start.place(x=150, y=250)

# TODO: add stop/pause functionality.
btn_stop = tk.Button(
	text="Stop Countdown",
	command=stop_button_command,
	cursor="X_cursor",
	height=2,
	width=10
	)

btn_stop.pack()
btn_stop.place(x=450, y=250)

prog = ttk.Progressbar(
	orient="horizontal",
	length=400,
	mode="determinate"
	)
prog.pack()
prog.place(x=150, y=200)

window.mainloop()
