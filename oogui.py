#!/bin/py
import tkinter 

class Counter:
	def _init_(self, parent): 
		self.parent = parent 
		self.frame = tkinter.Frame(parent)
		self.frame.pack()

		self.state = tkinter.IntVar()
		self.state.set(1)

		self.label = tkinter.Label(self.frame, textvariable=self.state)
		self.label.pack()

		self.up = tkinter.Button(self.frame, text='up', command=self.up_click)
		self.up.pack(side = 'left')

		self.right = tkinter.Button(self.frame, text='quit', command=self.quit_click)
		self.right.pack(side='left')

	def up_click(self): 
		self.state.set(self.state.get() +1)

	def quit_click(self):
		self.parent.destroy()

if __name__ == '__main__':
	window = tkinter.Tk()
	myapp = Counter(window)
	window.mainloop()	
