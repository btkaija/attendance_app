from tkinter import *
import tkinter as tk
import attendance_window
import database_options_window


class test:

	def __init__(self):
		self.main_window = Tk()
		self.main_window.title('test app')
		self.main_window.geometry('700x400+100+100')

		self.main_frame = Frame(self.main_window)
		self.main_frame.grid(column=0, row=0)

		welcome_label = tk.Label(self.main_frame, 
			text = "Welcome to the Test App", 
			font = ("Corbel", "20", "bold"), bg = 'red')
		welcome_label.grid(row = 0, column = 0, sticky=EW)

		description_label = tk.Label(self.main_frame,
			text = "Please choose an option above...",
			font = ("Corbel", "16", "italic"), bg = 'blue')
		description_label.grid(row = 2, column = 0, sticky=EW)
		
		Grid.grid_columnconfigure(self.main_window, 0, weight = 1)
		Grid.grid_rowconfigure(self.main_window, 0, weight = 1)

		# attendance_button = tk.Button(self.main_frame, 
		# 	text = "change frame", 
		# 	command = self.attendance_button_clicked,
		# 	font = ("Corbel", "16"), bg = 'green')
		# attendance_button.grid(row =1, column=0, padx = 20, pady = 20)
		# attendance_button.grid_columnconfigure(0, weight = 1)

		extra_label = tk.Label(self.main_frame, bg = 'black')
		extra_label.grid(row = 0, column = 1)
		self.main_window.mainloop()

	def attendance_button_clicked(self):
		print('button pressed')
		self.new_frame = Frame(self.main_window)
		new_label = tk.Label(self.new_frame, text = 'hello new frame!')
		new_label.grid(row = 1, column = 1)

		self.main_frame.grid_remove()
		self.new_frame.grid(row = 0, column = 0)




app = test()