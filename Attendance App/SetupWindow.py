from tkinter import *
import tkinter as tk
import WelcomeScreen
import OrganizationInformationScreen
import FinesScreen


class SetupWindow:
	def __init__(self):
		self.setup_window = Tk()
		self.setup_window.title('Greek Life Attendance Program Setup')
		self.setup_window.geometry('700x600+100+100')

		#set up the initial welcome screen
		self.welcome_frame = WelcomeScreen.WelcomeScreen(self.setup_window)
		self.welcome_frame.grid(row=0, column=0, columnspan = 2, padx=25, pady=25)
		#init the other screen for use later
		self.org_info_frame = OrganizationInformationScreen.OrganizationInformationScreen(self.setup_window)
		self.fines_screen = FinesScreen.FinesScreen(self.setup_window)

		self.screens = tuple((self.welcome_frame, self.org_info_frame, self.fines_screen))
		self.screen_index = 0

		self.back_button = Button(self.setup_window,
			command = self.backButtonPressed, 
			text = 'Back',
			state = DISABLED)
		self.back_button.grid(row=1, column = 0, padx=10, pady=10)

		self.next_button = Button(self.setup_window, 
			command = self.nextButtonPressed,
			text = 'Next')
		self.next_button.grid(row=1, column = 1, padx=10, pady=10)

		Grid.grid_columnconfigure(self.setup_window, 0, weight = 1)
		Grid.grid_rowconfigure(self.setup_window, 0, weight = 1)
		Grid.grid_columnconfigure(self.setup_window, 1, weight = 1)
		Grid.grid_rowconfigure(self.setup_window, 1, weight = 1)

		self.setup_window.mainloop()
	
	def backButtonPressed(self):
		if(self.screen_index == 0):
			print('Error, no more screens to go back to')
			return
		old_index = self.screen_index
		self.screen_index-=1
		self.updateScreen(old_index)

	def nextButtonPressed(self):
		if(self.screen_index == len(self.screens)-1):
			print('Error, no more screens next')
			return
		old_index = self.screen_index
		self.screen_index+=1
		self.updateScreen(old_index)

	def updateScreen(self, old_index):
		if(self.screen_index==0):
			self.back_button.config(state=DISABLED)
		else:
			self.back_button.config(state=ACTIVE)

		if(self.screen_index == len(self.screens)-1):
			self.next_button.config(state=DISABLED)
		else:
			self.next_button.config(state=ACTIVE)

		self.screens[old_index].grid_remove()
		self.screens[self.screen_index].grid(row=0, column=0, columnspan = 2, padx=25, pady=25)

setup = SetupWindow()