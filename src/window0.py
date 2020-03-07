from tkinter import *
from tkinter import messagebox

title = "Passwortgenerator"

def okButton_pressed():
	pass

def createWindow():
	window = Tk()
	window.title("Passwortgenerator")
	iconPath = "c:\\Users\\Christoph\\Desktop\\Python\\window_icon.ico"
	# Code to add widgets will go here...
	window.iconbitmap(iconPath)
	label0_text = "Passwortgenerator"
	label0 = Label ( window, text = label0_text)
	label0.config(font=("Arial", 30))
	label0.pack()

	window.mainloop()
	pass

createWindow()