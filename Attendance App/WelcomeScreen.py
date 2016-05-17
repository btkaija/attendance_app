from tkinter import *
import tkinter as tk
import defs

class WelcomeScreen(Frame):
	def __init__(self, parent, **options):
		Frame.__init__(self, parent, **options)

		
		self.welcome = Label(self, text = 'Welcome!', font = ('Corbel', '20', 'bold'))
		self.welcome.grid(row=0, column=0)
		self.info = Label(self,
			text = ('This is the Greek Life Attendance Program.\n '
			'A quick setup is required to use this program for your organization. '
			'\n\nInformation about who will be using this program  will be required. '
			"\n\nYour organization's attendance and fine policy will also need to be"
			'added in order to better utilize the features of this program. \n\nIf '
			'there are any issues with the program or the functionality of the'
			'program pleace contact Ben Kaija at btkaija@vt.edu. '
			'\n\nThank you for using the Greek Life Attendance Program!'
			"\n\nPlease click 'Next' to continue" ),
			font = defs.default_font,
			justify= LEFT,
			wraplength = 600)
		self.info.grid(row = 1, column=0)
