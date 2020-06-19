
from tkinter import *
from tkinter import messagebox
from vue.base_frame import BaseFrame


class SportsAddedFrame(BaseFrame):

    def __init__(self, member_controller, root_frame):
        super().__init__(root_frame)
        self._member_controller = member_controller
        self._create_widgets()
        self._members = None

    def _create_widgets(self):

        self.title = Label(self, text="List sports:")
        self.title.grid(row=0, column=0)

        # grille
        yDefil = Scrollbar(self, orient='vertical')
        self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=30, selectmode='single')
        yDefil['command'] = self.listbox.yview
        self.listbox.bind('<<ListboxSelect>>', self.onselect)
        yDefil.grid(row=1, column=1, sticky='ns')
        self.listbox.grid(row=1, column=0, sticky='nsew')


        self.menu = Button(self, text="Return", fg="red", command=self.back)
        self.menu.grid()

    def onselect(self, event):

        index = int(self.listbox.curselection()[0])
        print("selection", self._members[index])
        self.show_profile.grid(row=4, column=0)