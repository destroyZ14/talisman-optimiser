from tkinter import *
from tkinter import ttk

import glob

def reglob():
	global files
	files = glob.glob('loadouts/*.ld')

def edit(window):
	global files
	reglob()
	
	title = Label(window, text = "This tab allow you to manually edit loadouts.")
	title.grid(columnspan = 10)
	
	empty_file_error = Label(window, text = "")
	empty_file_error.grid()
    
	if not files:
		empty_file_error.configure(text = "You have no loadouts :(")
		return
		
	empty_file_error.configure(text = "")
	print(files)
	
	# Basedmg
	# Str
	# Critdmg
	# Crit chance (without tali ofc)
	# Bonus talisman stats <- need api alg
	# Tarantula
	# Superior
	# Sword/Bow
	# Combatlvl
	# Sharpness/smite/bane lvl
	# Ender slayer lvl
	# Power lvl :o
	# Drag hunter lvl