
from tkinter import *
from controller.person_controller import PersonController
from vue.base_frame import BaseFrame


class ListMembersFrame(BaseFrame):

    def __init__(self, person_controller: PersonController, root_frame: Frame, person_type: str = None):
        super().__init__(root_frame)
        self._person_controller = person_controller

        self._members = None
        if person_type is None:
            self._person_type = 'person'
        else:
            self._person_type = person_type
        self._create_widgets()

    def _create_widgets(self):

        self.title = Label(self, text="List members:")
        self.title.grid(row=0, column=0)

        # grille
        yDefil = Scrollbar(self, orient='vertical')
        self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=30, selectmode='single')
        yDefil['command'] = self.listbox.yview
        self.listbox.bind('<<ListboxSelect>>', self.onselect)
        yDefil.grid(row=1, column=1, sticky='ns')
        self.listbox.grid(row=1, column=0, sticky='nsew')

        # Return bouton
        self.show_profile = Button(self, text="Show profile", command=self.show_profile)
        self.menu = Button(self, text="Return", fg="red",
                           command=self.show_menu)
        self.menu.grid(row=4, column=0, sticky="w")

    def onselect(self, event):
        index = int(self.listbox.curselection()[0])
        print("selection", self._members[index])
        self.show_profile.grid(row=4, column=0)

    def show_profile(self):
        index = int(self.listbox.curselection()[0])
        member = self._members[index]
        self._root_frame.show_profile(member['id'])

    def show(self):
        self._members = self._person_controller.list_people(person_type = self._person_type)
        self.listbox.delete(0, END)
        for index, member in enumerate(self._members):
            text = member['firstname'].capitalize() + ' ' + member['lastname'].capitalize()
            self.listbox.insert(index, text)
        super().show()
