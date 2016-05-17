from tkinter import *
import tkinter as tk

class DatabaseOptionsWindow:

	def __init__(self):
		main_window = Tk()
		main_window.title("Database Options")
		main_window.geometry('700x400+100+100')

		main_frame = Frame()
		main_frame.grid(column=0, row=0)

		main_window.mainloop()

