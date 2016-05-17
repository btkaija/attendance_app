from tkinter import *
import tkinter as tk
import defs

class RepeatingEvent(Frame):
	def __init__(self, parent, **options):
		Frame.__init__(self, parent, **options)
		self.config(bg= '#ADADAD')

		self.info_label = Label(self,
			text = 'Please select how fines are distributed for this event',
			font = defs.default_font)
		self.info_label.grid(row = 0, column = 0, columnspan = 3)

		#init check boxes
		self.attended_checkbutton = Checkbutton(self, text ='Attended',
			font = defs.default_font, command = self.attendedChecked, width = 20)
		self.attended_checkbutton.grid(row = 1, column = 1)
		self.missed_checkbutton = Checkbutton(self, text ='Missed',
			font = defs.default_font, command = self.missedChecked, width = 20)
		self.missed_checkbutton.grid(row = 1, column = 2)
		self.percentage_checkbutton = Checkbutton(self, text = 'Percentage', 
			font = defs.default_font, command = self.percentageChecked, width = 20)
		self.percentage_checkbutton.grid(row=2, column = 0)
		self.number_checkbutton = Checkbutton(self, text = 'Number',
			font = defs.default_font, command = self.numberChecked, width = 20)
		self.number_checkbutton.grid(row=3, column = 0)

		#init text fields
		self.percent_attended_entry = Entry(self, width = 10, font = defs.default_font)
		self.percent_missed_entry = Entry(self, width = 10, font = defs.default_font)
		self.number_attended_entry = Entry(self, width = 10, font = defs.default_font)
		self.number_missed_entry = Entry(self, width = 10, font = defs.default_font)
		self.percent_attended_entry.grid(row = 2, column = 1)
		self.percent_missed_entry.grid(row = 2, column = 2)
		self.number_attended_entry.grid(row = 3, column = 1)
		self.number_missed_entry.grid(row= 3, column = 2)

	def percentageChecked(self):
		print('percent button')
	def numberChecked(self):
		print('number button')
	def attendedChecked(self):
		print('attended checked')
	def missedChecked(self):
		print('missed checked')

	def getStringOutput(self):
		return 'new repeating event'