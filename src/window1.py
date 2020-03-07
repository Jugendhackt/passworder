from tkinter import *
import Passwortgenerator

title = "Ergebnisse - passworder"

def passwordLoad(Password):
	pass

def replaceCharacters(replaceWith = []):
	pass

def createWindow(root, length):
	window1 = Toplevel(root)

	text0 = Label(window1, text = "Ihr Password ist:")
	text0.pack()

	password = Passwortgenerator.create(length)

	label1 = Label(window1, text = password)
	label1.config(font = ("Arial", 34))
	label1.pack()

	btnGenerateAgain = Button(window1, text = "Nochmal\ngenerieren", command = btnGenerateAgain_clicked)
	btnGenerateAgain.pack()

	btnCopyPassword = Button(window1, text = "Ins Zwischenablage kopieren", command = btnCopyPassword_clicked)
	btnCopyPassword.pack()

def btnGenerateAgain_clicked():
	pass

def btnCopyPassword_clicked():
	pass