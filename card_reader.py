import openpyxl

class CardReader:
	
	def __init__(self, filename = 'Pi_Kappa_Phi_Attendance.xslx'):
		f = filename
	
	def read_card():
		finalID = ''
		while(len(finalID) == 9):
			swipe = input("Please Swipe: ")
			swipes = swipe.split('=')
			finalID = swipes[0].strip(';')
		return finalID
	
	def contains_ID(value):
		is_present = 0
		wb = load_workbook(f)
		ws = wb.active
		ids = (ws.columns)[0]
		for i in range(1,len(ids)):
			if(value == ids[i].value)
			is_present = 1
		return bool(is_present == 1)	
	
	def add_ID(value, first_name, last_name):
		return True


