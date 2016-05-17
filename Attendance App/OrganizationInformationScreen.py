from tkinter import *
import tkinter as tk
import defs 

class OrganizationInformationScreen(Frame):
	def __init__(self, parent, **options):
		Frame.__init__(self, parent, **options)
		self.prompt = Label(self, 
			text = ('Please type the names and student ID numbers of the people who'
				'will be in charge of taking and managing attendance. '
				'Only the people added below will be able to login to this application'),
			font=('Corbel', '12'),
			wraplength=600,
			justify = LEFT)
		self.prompt.grid(row=0, column=0, columnspan = 2, padx = 25, pady = 25)

		self.org_name = Label(self, 
			text="Your Organization's Name: ",
			font = defs.default_font,
			width = 30,
			justify = LEFT)
		self.org_name.grid(row = 1, column = 0)

		self.org_name_field = Entry(self, width = 30)
		self.org_name_field.grid(row = 1, column = 1)

		self.name_label = Label(self, 
			text= 'Name of member',
			font = defs.default_font,
			width = 30)
		self.name_label.grid(row=2, column = 0)
		self.id_label = Label(self, 
			text = 'Student ID number',
			font = defs.default_font,
			width = 30)
		self.id_label.grid(row=2, column=1)

		self.default_name_field = Entry(self, width = 30, font = defs.default_font)
		self.default_name_field.grid(row=3, column = 0, padx = 5, pady = 5)
		self.default_id_field = Entry(self, width = 30, font = defs.default_font)
		self.default_id_field.grid(row=3, column=1, padx = 5, pady = 5)

		self.field_buttons_row = 4
		self.remove_field_button = Button(self, text = 'Remove Person', command = self.removeField, state = DISABLED, font = defs.default_font)
		self.remove_field_button.grid(row = self.field_buttons_row, column =0, padx =10, pady = 10, sticky = SE)
		self.add_field_button = Button(self, text = 'Add Person', command = self.addField, state = ACTIVE, font = defs.default_font)
		self.add_field_button.grid(row = self.field_buttons_row, column = 1, padx = 10, pady = 10, sticky = SW)

		self.name_fields = []
		self.id_fields = []

		##TEMP##
		self.save_button = Button(self, text='Save', command=self.saveOrgInfo)
		self.save_button.grid(row = 20, column = 0, columnspan= 2)
	
	def addField(self):
		self.field_buttons_row+=1
		if(self.field_buttons_row == 4): self.remove_field_button.config(state=DISABLED)
		else: self.remove_field_button.config(state=ACTIVE)
		self.remove_field_button.grid(row = self.field_buttons_row)
		self.add_field_button.grid(row =  self.field_buttons_row)
		self.name_fields.append(Entry(self, width = 30, font = defs.default_font))
		self.id_fields.append(Entry(self, width = 30, font = defs.default_font))
		for i in range(len(self.name_fields)):
			self.name_fields[i].grid(row = 4+i, column = 0, padx = 5, pady = 5)
			self.id_fields[i].grid(row = 4+i, column = 1, padx = 5, pady = 5)
		print('add field')
	
	def removeField(self):
		self.field_buttons_row-=1
		if(self.field_buttons_row == 4): self.remove_field_button.config(state=DISABLED)
		else: self.remove_field_button.config(state=ACTIVE)
		self.name_fields[len(self.name_fields)-1].grid_remove()
		self.id_fields[len(self.id_fields)-1].grid_remove()
		self.name_fields.pop()
		self.id_fields.pop()
		self.remove_field_button.grid(row = self.field_buttons_row)
		self.add_field_button.grid(row =  self.field_buttons_row)
		print('remove field')

	#stores data in the following format
	#<org name>
	#<name>_<ID#>
	#<name>_<ID#>
	def saveOrgInfo(self):
		print('saving...')
		temp_id = 0
		temp_name= ''
		self.login_file = open('login.dat', 'w')

		temp_name = self.org_name_field.get().replace('_', '-')
		self.login_file.write(temp_name+'\n')
		temp_id = self.parse_id_data(self.default_id_field.get())
		if(temp_id == 'invalid'):
			print('unable to save data')
			return
		self.login_file.write(self.default_name_field.get()+'_'+temp_id+'\n')
		
		for i in range(len(self.name_fields)):
			temp_name = self.org_name_field.get().replace('_', '-')
			self.login_file.write(temp_name+'_')
			temp_id = self.parse_id_data(self.id_fields[i].get())
			if(temp_id == 'invalid'):
				print('unable to save data')
				return
			else:
				self.login_file.write(temp_id+'\n')
		self.login_file.close()

	# Will either return a nine diget ID number or 'invalid'
	def parse_id_data(self, swipe):
		#normal swipe is formatted as ;XXXXXXXXX=XXXX?
		#faulty swipe %E?;XXXXXXXXX=XXXX? or ;E? or ;E?+E? or +E?
		try:
			if len(swipe) == 9:
				return swipe
			elif len(swipe) == 16:
				normal_swipe = swipe.split('=')[0].split(';')[1]
				if len(normal_swipe) != 9:
					normal_swipe = 'invalid'
				return normal
				_swipe
			elif len(swipe) == 19:
				errored_swipe = swipe.split(';')[1].split('=')[0]
				if len(errored_swipe) != 9:
					errored_swipe = 'invalid'
				return errored_swipe
			else:
				return 'invalid'
		except:
			print('format error')
			return 'invalid'
		



