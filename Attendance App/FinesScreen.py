from tkinter import *
import tkinter as tk
import defs
import RepeatingEventFrame

class FinesScreen(Frame):
	def __init__(self, parent, **options):
		Frame.__init__(self, parent, **options)
		self.promt = Label(self,
			text = ('This is where you will create the different events that you plan '
				'to have over the course of the year/semester. You will be givin the opportunity'
				' to add more events if you forget any.'
				'\n\nFor repeating events you will need to know one of the following:\n'
				'- What percent of events can be missed before a member is fined?\n'
				'- What percent of events need to be attended so a member does not get fined\n'
				'- What number of events can be missed before a member is fined?\n'
				'- What number of events need to be attended so a member does not get fined'),
			font = defs.default_font,
			wraplength=600,
			justify = LEFT)
		self.promt.grid(row = 0, column = 0, columnspan = 4)

		self.add_event_button = Button(self, text = 'Add Event', width = 15, command = self.addEvent, font = defs.default_font)
		self.add_event_button.grid(row = 2, column = 0, columnspan = 2, sticky = SE, padx = 10, pady = 10)
		self.remove_event_button = Button(self, text = 'Remove Event', width = 15, command = self.removeEvent, font=  defs.default_font, state = DISABLED)
		self.remove_event_button.grid(row = 2, column = 2, columnspan = 2, sticky = SW, padx = 10, pady =10)

		self.event_name_label = Label(self, text = 'Event Name', font = defs.default_font)
		self.event_name_label.grid(row = 1, column = 0)
		self.fine_amount_label = Label(self, text = 'Fine Amount', font = defs.default_font)
		self.fine_amount_label.grid(row = 1, column = 1)
		self.repeating_label = Label(self, text = 'Repeating?', font= defs.default_font)
		self.repeating_label.grid(row = 1, column = 2)

		self.add_button_row = 2

		self.event_names = []
		self.fine_amounts = []
		self.repeating_checkbuttons = []
		self.edit_done_buttons = []
		self.repeating_event_frames = []

		self.checkbuttons_selected = []
		self.repeating_frame_open = []

	def addEvent(self):
		self.add_event_button.grid(row = self.add_button_row+2)
		self.remove_event_button.grid(row = self.add_button_row+2)
		#create and add new fields to lists
		field_row = self.add_button_row
		self.event_names.append(Entry(self, width = 30, font = defs.default_font))
		self.fine_amounts.append(Entry(self, width = 10, font = defs.default_font))
		self.repeating_checkbuttons.append(Checkbutton(self, text = '', font = defs.default_font,
			command = lambda: self.repeatingChecked(field_row)))
		self.edit_done_buttons.append(Button(self, text = 'Edit', width = 15, font = defs.default_font,
			command = lambda: self.modifyEvent(field_row), state = DISABLED))

		self.checkbuttons_selected.append(False)
		self.repeating_frame_open.append(False)

		i = len(self.event_names)-1
		self.event_names[i].grid(row = self.add_button_row, column = 0, padx = 5, pady = 5)
		self.fine_amounts[i].grid(row = self.add_button_row, column = 1, padx = 5, pady = 5)
		self.repeating_checkbuttons[i].grid(row = self.add_button_row, column = 2, padx = 5, pady = 5)
		self.edit_done_buttons[i].grid(row = self.add_button_row, column = 3, padx = 5, pady = 5)
		
		self.add_button_row+=2

		if(len(self.event_names) == 0): 
			self.remove_event_button.config(state = DISABLED)
		else: 
			self.remove_event_button.config(state = ACTIVE)


	def removeEvent(self):
		self.event_names[len(self.event_names)-1].grid_remove()
		self.fine_amounts[len(self.fine_amounts)-1].grid_remove()
		self.repeating_checkbuttons[len(self.repeating_checkbuttons)-1].grid_remove()
		self.edit_done_buttons[len(self.edit_done_buttons)-1].grid_remove()

		self.event_names.pop()
		self.fine_amounts.pop()
		self.repeating_checkbuttons.pop()
		self.edit_done_buttons.pop()

		self.checkbuttons_selected.pop()
		self.repeating_frame_open.pop()

		self.add_button_row-=2
		self.add_event_button.grid(row = self.add_button_row)
		self.remove_event_button.grid(row = self.add_button_row)

		if(len(self.event_names) == 0): 
			self.remove_event_button.config(state = DISABLED)
		else: 
			self.remove_event_button.config(state = ACTIVE)

	def modifyEvent(self, row):
		index = int(row/2) - 1
		if(self.repeating_frame_open[index]):
			self.edit_done_buttons[index].config(text = 'Edit')
			self.repeating_event_frames[len(self.repeating_event_frames)-1].grid_remove()
			self.repeating_frame_open[index] = False
		else:
			self.edit_done_buttons[index].config(text = 'Done')
			self.repeating_event_frames[len(self.repeating_event_frames)-1].grid(row = row+1, column = 0, columnspan = 4)
			self.repeating_frame_open[index] = True

	def repeatingChecked(self, row):
		index = int(row/2) - 1
		if(self.checkbuttons_selected[index]):
			self.checkbuttons_selected[index] = False
			self.edit_done_buttons[index].config(state = DISABLED, text = 'Edit')
			self.repeating_event_frames[len(self.repeating_event_frames)-1].grid_remove()
			self.repeating_event_frames.pop()
			self.repeating_frame_open[index] = False
		else:
			self.checkbuttons_selected[index] = True
			self.edit_done_buttons[index].config(state = ACTIVE, text = 'Done')
			self.repeating_event_frames.append(RepeatingEventFrame.RepeatingEvent(self))
			self.repeating_event_frames[len(self.repeating_event_frames)-1].grid(row = row+1, column = 0, columnspan = 4)
			self.repeating_frame_open[index] = True


		






