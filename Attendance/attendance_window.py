from tkinter import *
import tkinter as tk
import parse_card_data
import time
import datetime

class AttendanceWindow:

	def __init__(self):
		
		self.main_window = Tk()
		self.main_window.title("Attendance")
		#self.main_window.geometry('700x400+100+100')
		#self.main_window.resizable(width=FALSE, height=FALSE)

		main_frame = Frame(self.main_window)
		main_frame.grid(row=0, column=0)

		self.event_name_label = Label(main_frame,
			text = "What is the name of this event?",
			font = ("Corbel", "12"))
		self.event_name_label.grid(row = 0, column = 0)

		self.event_name_box = Entry(main_frame,
			font =("Corbel", "12"),
			width = 15)
		self.event_name_box.grid(row = 0, column = 1)

		self.event_name_button = Button(main_frame,
			font =("Corbel", "12"),
			text = "Confirm",
			command = self.button_toggle)
		self.event_name_button.grid(row = 0, column = 2)

		self.name_confirmed = False

		swipe_label = tk.Label(main_frame,
			text = "Please Swipe Your Hokie Passport...",
			font = ("Corbel", "20", "bold"))
		swipe_label.grid(row = 1, column = 0, padx = 30, pady = 30, columnspan = 3)

		self.id_label = tk.Label(main_frame,
			text = "ID# = ---------",
			font = ("Corbel", "20", "italic"))
		self.id_label.grid(row = 3, column = 0, columnspan = 3)

		self.name_label = Label(main_frame,
			text = 'Welcome, ---------!',
			font = ("Corbel", "20", "italic"))
		self.name_label.grid(row = 4, column = 0, columnspan = 3)

		self.count_label = Label(main_frame,
			text = "Attendance Count: 0", 
			font = ("Corbel", "20", "italic"))
		self.count_label.grid(row = 5, column = 0, columnspan = 3)


		self.id_textbox = tk.Entry(main_frame,
			width = 20,
			state = DISABLED,
			font = ("Corbel", "16", "bold")
			)
		self.id_textbox.grid(row = 2, column = 0, pady = 30, columnspan = 3)
		self.id_textbox.focus_set()

		self.id_textbox.bind("<Return>", self.on_enter_pressed)
		
		self.attendance_record = []
		self.rushes_record = []
		#this runs continuously parallel with mainloop()
		
		self.main_window.mainloop()
	def button_toggle(self):
		if(self.name_confirmed):
			self.name_confirmed = False
			self.event_name_box.config(state = NORMAL)
			self.id_textbox.config(state = DISABLED)
			self.event_name_button.config(text = "Confirm")
		else:
			if('Rushes' in self.event_name_box.get()):
				self.event_name_button.flash()
				return
			self.name_confirmed = True
			self.event_name_box.config(state = DISABLED)
			self.id_textbox.config(state = NORMAL)
			self.event_name_button.config(text = "Change")
			self.init_records()
			
	def init_records(self):
		date = time.strftime("%x").replace('/', '-')
		try:
			bro_data = open('data/'+self.event_name_box.get()+'_'+date+'.dat')
			bro_lines = bro_data.readlines()
			for i in range(len(bro_lines)):
				id_num = bro_lines[i].split('_')[0]
				name = bro_lines[i].split('_')[1].strip()
				self.attendance_record.append((id_num, name))
		except FileNotFoundError:
			pass
		try:
			rush_data = open('data/'+self.event_name_box.get()+'_Rushes_'+date+'.dat')
			rush_lines = rush_data.readlines()
			for i in range(len(rush_lines)):
				id_num = rush_lines[i].split('_')[0]
				name = rush_lines[i].split('_')[1].strip()
				email = rush_lines[i].split('_')[2]
				phone = rush_lines[i].split('_')[3]
				grad_year = rush_lines[i].split('_')[4]
				self.rushes_record.append((id_num, name, email, phone, grad_year))
		except FileNotFoundError:
			pass

		self.count_label.config(text = "Attendance Count: "+str(len(self.attendance_record)+len(self.rushes_record)))



	def on_enter_pressed(self, event):
		#print(self.id_textbox.get(), " is the value when enter pressed")
		event_name = self.event_name_box.get()
		input_value = self.id_textbox.get()
		id_num = parse_card_data.parse_card_data(input_value)
		self.id_label.config(text = "ID# = "+id_num)
		self.id_textbox.delete(0, len(input_value))
		if(id_num == 'invalid'):
			return
		else:
			brother = self.checkIDs(id_num)
		if(brother == 'invalid'):
			rush = self.check_rush(id_num)
			if(rush == 'invalid'):
				self.add_brother(id_num)
			else:
				self.check_rush_list(id_num, rush, self.get_email(id_num), self.get_phone(id_num), self.get_grad_year(id_num))
				self.name_label.config(text = 'Welcome, '+rush+'!')
				self.count_label.config(text = "Attendance Count: "+str(len(self.attendance_record)+len(self.rushes_record)))
		else:
			#check if already on list otherwise add
			self.check_list(id_num, brother)
			self.update_file(brother)


	def checkIDs(self, num):
		master_list = open('IDs.dat')
		lines = master_list.readlines()
		id_nums = []
		names = []
		for i in range(len(lines)):
			id_nums.append(int(lines[i].split('_')[0]))
			names.append(lines[i].split('_')[1])
			if(int(num) == id_nums[i]):
				return names[i].strip()
		return 'invalid'
		master_list.close()

	def update_file(self, name):
		date = time.strftime("%x").replace('/', '-')
		data = open('data/'+self.event_name_box.get()+'_'+date+'.dat', 'w+')
		for i in range(len(self.attendance_record)):
			data.write(self.attendance_record[i][0]+'_')
			data.write(self.attendance_record[i][1]+'\n')
		data.close()
		self.name_label.config(text = 'Welcome, '+name+'!')
		self.count_label.config(text = "Attendance Count: "+str(len(self.attendance_record)+len(self.rushes_record)))

	def check_list(self, id_num, name):
		for i in range(len(self.attendance_record)):
			if(id_num == self.attendance_record[i][0]):
				return
		#else add to list
		#if(id_num == '905617961' or id_num == '905614629' or id_num == '905580445'):
		#	return
		self.attendance_record.append((id_num, name))

	def check_rush_list(self, id_num, name, email, phone, grad_year):
		for i in range(len(self.rushes_record)):
			if(id_num == self.rushes_record[i][0]):
				break
		else:
			self.rushes_record.append((id_num, name, email, phone, grad_year))

	def add_brother(self, id_num):
		self.name_window = Tk()
		self.name_window.title("Add Name")
		self.name_window.resizable(width=FALSE, height=FALSE)
		self.name_window.lift()
		self.name_input_label = Label(self.name_window, font = ("Corbel", "12"), text = "Name:\n(First and Last)")
		self.name_input_label.grid(row = 1, column = 0, padx = 5, pady = 5)
		self.name_field = Entry(self.name_window, width = 20, font =("Corbel", "12"))
		self.name_field.grid(row = 1, column = 1, padx = 5, pady = 5)

		self.rush_email_label = Label(self.name_window, font = ("Corbel", "12"), text = "Email:")
		self.rush_phone_label = Label(self.name_window, font = ("Corbel", "12"), text = "Phone:")
		self.rush_year_label = Label(self.name_window, font = ("Corbel", "12"), text = "Graduation Date\n(Freshman, Sophmore, Junior, Senior):")
		self.rush_email = Entry(self.name_window, font = ("Corbel", "12"))
		self.rush_phone = Entry(self.name_window, font = ("Corbel", "12"))
		self.rush_year = Entry(self.name_window, font = ("Corbel", "12"))

		self.isBro = True
		self.rush_checkbox = Checkbutton(self.name_window, font =("Corbel", "12"), command = self.rush_checked, text = "Rush")
		self.bro_checkbox = Checkbutton(self.name_window, font =("Corbel", "12"), command = self.bro_checked, text = "Brother")
		self.bro_checkbox.select()
		self.rush_checkbox.grid(row = 5, column = 1, padx = 5, pady = 5)
		self.bro_checkbox.grid(row = 5, column = 0, padx = 5, pady = 5)

		self.done_button = Button(self.name_window, font =("Corbel", "12"), text = "Done", command = lambda: self.close_name_window(id_num))
		self.done_button.grid(row = 6, column = 0, columnspan = 2, padx = 5, pady = 5)
	
	def close_name_window(self, id_num):
		if(self.isBro):
			master_list = open('IDs.dat', 'a')
			master_list.write(id_num + '_'+self.name_field.get()+'\n')
			self.check_list(id_num, self.name_field.get())
			self.update_file(self.name_field.get())
		else:
			name = self.name_field.get()
			email = self.rush_email.get()
			phone = self.rush_phone.get()
			grad_year = self.rush_year.get()

			date = time.strftime("%x").replace('/', '-')
			this_rush_list = open('data/'+self.event_name_box.get()+'_Rushes_'+date+'.dat', 'w+')
			master_rush = open("Rushes.dat", 'a')
			self.check_rush_list(id_num, name, email, phone, grad_year)
			for i in range(len(self.rushes_record)):
				this_rush_list.write(self.rushes_record[i][0]+'_')
				this_rush_list.write(self.rushes_record[i][1]+'_')
				this_rush_list.write(self.rushes_record[i][2]+'_')
				this_rush_list.write(self.rushes_record[i][3]+'_')
				this_rush_list.write(self.rushes_record[i][4]+'\n')
			#add to master list
			master_rush.write(self.rushes_record[i][0]+'_')
			master_rush.write(self.rushes_record[i][1]+'_')
			master_rush.write(self.rushes_record[i][2]+'_')
			master_rush.write(self.rushes_record[i][3]+'_')
			master_rush.write(self.rushes_record[i][4]+'\n')
			master_rush.close()
			this_rush_list.close()
			self.name_label.config(text = 'Welcome, '+name+'!')
			self.count_label.config(text = "Attendance Count: "+str(len(self.attendance_record)+len(self.rushes_record)))
		self.name_window.destroy()

	def check_rush(self, id_num):
		data = open('Rushes.dat')
		lines = data.readlines()
		for i in range(len(lines)):
			if(id_num == lines[i].split('_')[0]):
				return lines[i].split('_')[1].strip()
		else:
			return 'invalid'
	def get_email(self, id_num):
		data = open("Rushes.dat")
		lines = data.readlines()
		for i in range(len(lines)):
			if(id_num == lines[i].split('_')[0]):
				return lines[i].split('_')[2]
		return
	def get_phone(self, id_num):
		data = open("Rushes.dat")
		lines = data.readlines()
		for i in range(len(lines)):
			if(id_num == lines[i].split('_')[0]):
				return lines[i].split('_')[3]
		return

	def get_grad_year(self, id_num):
		data = open("Rushes.dat")
		lines = data.readlines()
		for i in range(len(lines)):
			if(id_num == lines[i].split('_')[0]):
				return lines[i].split('_')[4]
		return
	def rush_checked(self):
		self.bro_checkbox.deselect()
		self.isBro = False
		self.rush_email_label.grid(row = 2, column = 0, padx = 5, pady = 5)
		self.rush_email.grid(row = 2, column = 1, padx = 5, pady = 5)
		self.rush_phone_label.grid(row = 3, column = 0, padx = 5, pady = 5)
		self.rush_phone.grid(row = 3, column = 1, padx = 5, pady = 5)
		self.rush_year_label.grid(row = 4, column = 0, padx = 5, pady = 5)
		self.rush_year.grid(row = 4, column = 1, padx = 5, pady = 5)
	def bro_checked(self):
		self.isBro = True
		self.rush_checkbox.deselect()
		self.rush_email_label.grid_remove()
		self.rush_email.grid_remove()
		self.rush_phone_label.grid_remove()
		self.rush_phone.grid_remove()
		self.rush_year.grid_remove()
		self.rush_year_label.grid_remove()
