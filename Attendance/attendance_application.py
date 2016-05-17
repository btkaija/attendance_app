from tkinter import *
import tkinter as tk
import attendance_window
import database_options_window


class AttendanceApplication:

	def __init__(self):
		main_window = Tk()
		main_window.title('Pi Kappa Phi Brotherhood Attendance')
		#main_window.geometry('700x400+100+100')
		#main_window.resizable(width=FALSE, height=FALSE)

		main_frame = Frame(main_window)
		main_frame.grid(column=0, row=0)

		welcome_label = tk.Label(main_frame, 
			text = "Welcome to the Pi Kappa Phi Brotherhood Database!", 
			font = ("Corbel", "20", "bold"))
		welcome_label.grid(row = 1, column = 1, padx = 32, pady = 32)

		description_label = tk.Label(main_frame,
			text = "Please choose an option above...",
			font = ("Corbel", "16", "italic"))
		description_label.grid(row = 5, column = 1, padx = 32, pady = 32)

		attendance_button = tk.Button(main_frame, 
			text = "Take Attendance", 
			command = self.attendance_button_clicked,
			font = ("Corbel", "16"))
		attendance_button.grid(row =2, column=1, padx = 20, pady = 20)

		database_options_button = tk.Button(main_frame, 
			text = "Export to Excel", 
			command = self.database_options_button_clicked,
			font = ("Corbel", "16"))
		database_options_button.grid(row = 3, column = 1, padx = 20, pady = 20)

		main_window.mainloop()

	def attendance_button_clicked(*args):
		attendance_window.AttendanceWindow()

	def database_options_button_clicked(*args):
		database_options_window.DatabaseOptionsWindow()

