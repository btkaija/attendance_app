from tkinter import *
import tkinter as tk
import time
import datetime

class AttendanceWindow:

	def __init__(self):
		self.main_window = Tk()
		self.main_window.title("Attendance")
		self.main_window.geometry('500x400+100+100')
		self.main_window.resizable(width=FALSE, height=FALSE)

		main_frame = Frame(self.main_window)
		main_frame.grid(row=0, column=0)

		swipe_label = tk.Label(main_frame,
			text = "Please Swipe Your Hokie Passport...",
			font = ("Corbel", "20", "bold"))
		swipe_label.grid(row = 1, column = 1, padx = 30, pady = 30)

		self.id_label = tk.Label(main_frame,
			text = "ID# = ---------",
			font = ("Corbel", "20", "italic"))
		self.id_label.grid(row = 3, column = 1, pady = 30)

		self.id_textbox = tk.Entry(main_frame,
			width = 20,
			state = NORMAL,
			font = ("Corbel", "16", "bold")
			)
		self.id_textbox.grid(row = 2, column = 1, pady = 30)
		self.id_textbox.focus_set()

		self.id_textbox.bind("<Return>", self.on_enter_pressed)
		
		#this runs continuously parallel with mainloop()
		self.update_labels()
		self.main_window.mainloop()
	
	def on_enter_pressed(self, event):
		print(self.id_textbox.get(), " is the value when enter pressed")
		input_value = self.id_textbox.get()
		id_num = self.parse_id_data(input_value)
		self.id_label.config(text = "ID# = "+id_num)
		self.id_textbox.delete(0, len(input_value))

	def update_labels(self):
		#date
		print(time.strftime("%x"))
		#time
		print(time.strftime("%X"))
		#datetime
		print(datetime.datetime.now())

	# Will either return a nine diget ID number or 'invalid'
	def parse_id_data(self, swipe):
		#normal swipe is formatted as ;XXXXXXXXX=XXXX?
		#faulty swipe %E?;XXXXXXXXX=XXXX? or ;E? or ;E?+E? or +E?
		if len(swipe) == 9:
			return swipe
		elif len(swipe) == 16:
			normal_swipe = swipe.split('=')[0].split(';')[1]
			if len(normal_swipe) != 9:
				normal_swipe = 'invalid'
			return normal_swipe
		elif len(swipe) == 19:
			errored_swipe = swipe.split(';')[1].split('=')[0]
			if len(errored_swipe) != 9:
				errored_swipe = 'invalid'
			return errored_swipe
		else:
			return 'invalid'



