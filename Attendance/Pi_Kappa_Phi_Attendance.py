from openpyxl import *
from tkinter import *
from tkinter import ttk
import card_reader


IDnum = 'invalid'
print("What event is this for?")
eventName = input("Format (NAME MM/DD/YYYY) = ")
reader = card_reader.CardReader()
correct_name_flag = False
event_index = reader.contains_event_name(eventName)
if(event_index == -1):
	reader.add_event(eventName)
	event_index = reader.contains_event_name(eventName)
while(1):

	while(IDnum == 'invalid'):
		swipe_val = input("Please Swipe ... ")
		IDnum = reader.read_card(swipe_val)
		print(IDnum, ' swipe')

	if(not(reader.contains_ID(IDnum))):
		while(not(correct_name_flag)):
			#pledge = input('Pledge (y/n) ? ')
			first_name = input('First name: ')
			last_name = input('Last name: ')
			# if(pledge == 'y'):
			# 	correct_name_flag = reader.add_person_to_doc(IDnum, first_name, last_name)
			# else:
			correct_name_flag = reader.add_ID_to_name(IDnum, first_name, last_name)
		correct_name_flag = False
	print("Welcome,", reader.get_first_name_from_ID(IDnum), reader.get_last_name_from_ID(IDnum))
	reader.set_attended(IDnum, event_index)
	IDnum = 'invalid'
print("end loop")
