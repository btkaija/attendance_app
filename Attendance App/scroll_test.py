from tkinter import *  

class scroll_test:
	def __init__(self):
		master = Tk()

		master.geometry('400x400+100+100')
		master.grid_rowconfigure(0,weight = 1)
		master.grid_columnconfigure(0, weight = 1)


		self.main_frame = Frame(master, width = 100, height = 100)
		self.main_frame.grid(row = 0, column = 0)
		#self.main_frame.grid_propagate(0)

		# self.main_frame.grid_rowconfigure(1, weight = 1)
		# self.main_frame.grid_columnconfigure(0, weight = 1)

		add_button = Button(self.main_frame, text = 'add', command = self.add)
		remove_button = Button(self.main_frame, text = 'remove', command = self.remove)
		add_button.grid(row = 0, column = 0, sticky = NW)
		remove_button.grid(row = 0, column = 1, sticky = NW)


		self.canvas = Canvas(self.main_frame, width = 200, height = 200, bg = 'red')
		self.canvas.grid(row = 1, column = 0, columnspan = 2)
		#self.canvas.grid_propagate(0)

		v_scrollbar = Scrollbar(self.canvas, orient = VERTICAL)
		v_scrollbar.grid(row = 0, column = 1, sticky = E+N+S, rowspan = 2)

		h_scrollbar = Scrollbar(self.canvas, orient = HORIZONTAL)
		h_scrollbar.grid(row=1, column = 0, sticky = S+E+W)

		self.canvas.config(yscrollcommand = v_scrollbar.set, xscrollcommand = h_scrollbar.set)
		v_scrollbar.config(command=self.canvas.yview)
		h_scrollbar.config(command=self.canvas.xview)
		#self.canvas.config(scrollregion=(0, 0, 100, 100))

		self.myframe = Frame(self.canvas)
		self.myframe.grid(row = 0, column = 0, sticky = N+E+S+W)

		# self.canvas.grid_columnconfigure(1, weight = 1)
		# self.canvas.grid_rowconfigure(0, weight = 1)

		# master.grid_rowconfigure(1, weight=1)
		# master.grid_columnconfigure(0, weight=1)

		

		

		self.labels = []
		self.count = 0
		self.add()
		mainloop()

	def add(self):
		print('add')
		self.labels.append(Label(self.myframe, text = self.count))
		self.labels[self.count].grid(row = self.count, column = 0, columnspan = 2)
		self.count+=1

	def remove(self):
		print('remove')
		self.count-=1
		self.labels[self.count].grid_remove()
		self.labels.pop()

test = scroll_test()



