from tkinter import *
from tkinter import ttk
import skypy

# This is my personal API key, if you want one please use /api ingame
key = '672fbd69-cae7-4911-881b-76e120d383ea'
hypixel = skypy.Player(key)

def api(window):    
	title = Label(window, text = "This tab will import all of your stats from hypixel's api.")
	title.grid(columnspan = 10)
	
	# Get profile
	
	def get_profile():
		hypixel.set_uname(name_input.get())
		profiles = hypixel.player_profiles()
		
		if not profiles:
			error.configure(text = "Not a real player!")
		else:
			error.configure(text = "")
			if len(profiles) == 1:
				hypixel.set_profile(list(profiles.values())[0])
				use_profile()
			else:
				profile_l = Label(window, text = "Which profile should I use?")
				profile_l.grid(row = 2, sticky = W)
				
				def choose_profile():
					hypixel.set_profile(profiles[profile_input.get()])
					use_profile()
					
				profile_input = ttk.Combobox(window, values = list(profiles.keys()))
				profile_input.grid(column = 1, row = 2, sticky = W)
				profile_input.bind("<<ComboboxSelected>>", (lambda event: choose_profile()))
	
	name_l = Label(window, text = "What is your username?")
	name_l.grid(sticky = W)
	name_input = Entry(window, width = 10)
	name_input.grid(column = 1, row = 1, sticky = W)
	name_input.bind("<Return>", (lambda event: get_profile()))
	
	error = Label(window, text = "")
	error.grid(column = 2, row = 1, sticky = E)
	
	# Format data
	
	def use_profile():
		print(hypixel.player_stats())