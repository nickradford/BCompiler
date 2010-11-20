from Tkinter import *
import tkFileDialog
import tkMessageBox
import os, sys, shlex
from subprocess import Popen, PIPE
import BParser
import pdb
def buildGUI():
	root = Tk(className=" B Compiler v0.0.1")
	
	fileIOFrame = Frame(root, width="400", height="100")
	fileIOFrame.grid(row="0", column="0")
	
	global fileName
	fileName = Label(fileIOFrame, text="Click to open file", fg="#000", width="32", relief="groove")
	fileName.grid(row="0", column="0")
	fileName.bind("<Button-1>", openFile)
	
	openFileBtn = Button(fileIOFrame, text="Compile", command=compile)
	openFileBtn.grid(row="0", column="1")
	
	global runJavaBtn
	runJavaBtn = Button(fileIOFrame, text="Run Java", state="disabled", command=run)
	runJavaBtn.grid(row="2", column="1", sticky="W")
	
	
	global console
	console = Text(root, width="50", height="10", bg="#333333", fg="#DDDDDD", font="Courier", insertwidth="6", insertbackground="#DDDDDD", takefocus="0")
	console.grid(row="1", column="0")
	console.insert(END, "")

	return root

def openFile(self):
	global fn
	fn = tkFileDialog.askopenfilename(parent=root, title="Open a .b program...", filetypes=[("B Program", "*.b")])
	fileName.config(text=fn)
	
def compile():
	#try:
		#pdb.set_trace()
		bp = BParser.BParser(fn)
		bp.compile()
		runJavaBtn.config(state="normal")
	#except:
		#console.insert(END, "Oops")
	
def run():
	cmd = "java run"
	args = shlex.split(cmd)
	p = Popen(args, stdout=PIPE)
	console.insert(END,p.communicate()[0])


root = buildGUI()

root.mainloop()