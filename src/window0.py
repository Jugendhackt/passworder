from tkinter import *
import window1

title = "Password generieren - passworder"

root = Tk()
variableCharacterReplacement = BooleanVar(root)
frame1 = Frame(root)
spinbox = Spinbox(frame1, from_ = 1, to = 100, wrap = True)
characterReplacement = Checkbutton(root, text = "Zeichen ersetzen", variable = variableCharacterReplacement)

def okButton_pressed():
	window1.createWindow(root, int(spinbox.get()))

def addItemButton_pressed():
	pass

def createWindow():
	root.title("Passwortgenerator")

	label0_text = "Passwortgenerator"
	label0 = Label(root, text = label0_text)
	label0.config(font = ("Arial", 34))
	label0.pack()

	characterReplacement.pack()

	frame0 = Frame(root)
	frame0.pack()

	characterInput0 = Entry(frame0)
	characterInput0.pack(side=LEFT)

	characterInput1 = Entry(frame0)
	characterInput1.pack(side=LEFT)

	btnAddItem = Button(frame0, text="Hinzufügen", command=addItemButton_pressed)
	btnAddItem.pack(side=RIGHT)

	btnOk = Button(root, text="Generieren", command=okButton_pressed)
	btnOk.pack(side=BOTTOM)

	newOrder = (characterReplacement, characterInput0, characterInput1)
	for widget in newOrder:
		widget.lift()

	frame1.pack()

	label1 = Label(frame1, text = "Mindestlänge des Passworts")
	label1.pack(side = LEFT)

	spinbox.pack(side = RIGHT)

	root.mainloop()

createWindow()