from Tkinter import *
import tkFileDialog
import tkMessageBox
import os, sys, shlex, shutil, time
from subprocess import Popen, PIPE
import BParser
import pdb
from CompilerException import *
def buildGUI():
	root = Tk()
	root.title("B Compiler v0.0.1")
	root.geometry("408x194-300+200")
	root.resizable(0,0)
	
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
	err = False
	#pdb.set_trace()
	start = time.time()
	shutil.copy(fn, "_temp.b")
	with open("_temp.b", 'a') as f:
		f.write("#EOF;");
	
	bp = BParser.BParser("_temp.b")
	try:
		bp.compile()
		runJavaBtn.config(state="normal")
	except Exception, e:
		if bp.debugging():
			bp.bs._symbols.dump()
		console.insert(END, str(e) + '\n')
		err = True
	finally:
		if bp.debugging():
			bp._debugFile.close()
		os.remove("_temp.b")
		del bp
		end = time.time()
		elapsed = end - start
	
	if not err:
		console.insert(END, "Program successfully compiled in " + str(int(10 * elapsed)) + " seconds.\n")
	
		
	
def run():
	cmd = "java run"
	args = shlex.split(cmd)
	p = Popen(args, stdout=PIPE)
	console.insert(END,p.communicate()[0])


root = buildGUI()

root.mainloop()