from tkinter import *
from tkinter import ttk

from create import create
from load import load
from delete import delete
from edit import edit
from api import api

master = Tk()
master.title("Talisman Optmiser")
master.geometry('800x600')

tab_control = ttk.Notebook(master)


def create_frame(label, function):
    frame = ttk.Frame(tab_control)
    tab_control.add(frame, text=label)
    function(frame)


create_frame('Create Loadout', create)
create_frame('Load Loadout', load)
create_frame('Delete Loadout', delete)
create_frame('Edit Loadout', edit)
create_frame('Import Loadout', api)

tab_control.pack(expand=1, fill='both')

master.mainloop()
