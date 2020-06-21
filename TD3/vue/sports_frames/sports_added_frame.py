
from tkinter import *
from tkinter import messagebox
from vue.base_frame import BaseFrame

class SportsAddedFrame(BaseFrame):

    def __init__(self, sport_controller, person_controller, root_frame):
        super().__init__(root_frame)
        self._sport_controller = sport_controller
        self._person_controller = person_controller
        self._create_widgets()
        self._sports = None
        self.assign_coach = Button(self, text="Assign coach...", command=self.assign_coach)
        self.delete_sport = Button(self, text="Delete", foreground='red', command=self.delete_sport)
        self.delete_coach = Button(self, text="Delete", foreground='red', command=self.delete_coach)
        self.current_sport = None


    def _create_widgets(self):

        self.titleSports = Label(self, text="Select a Sport :")
        self.titleSports.grid(row=0, column=0)

        self.titleCoachs = Label(self, text="Select a Coach :")

        # grille
        yDefil = Scrollbar(self, orient='vertical')
        self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=30, selectmode='single',selectbackground='green', exportselection=False)
        yDefil['command'] = self.listbox.yview
        self.listbox.bind('<<ListboxSelect>>', self.onselect)
        yDefil.grid(row=1, column=1, sticky='ns')
        self.listbox.grid(row=1, column=0, sticky='nsew')

        self.yDefilCoach = Scrollbar(self, orient='vertical')
        self.listboxCoach = Listbox(self, yscrollcommand=self.yDefilCoach.set, width=30, selectmode='single',selectbackground='green', exportselection=False)
        self.yDefilCoach['command'] = self.listboxCoach.yview
        self.listboxCoach.bind('<<ListboxSelect>>', self.onselectCoachs)

        self.menu = Button(self, text="Return", fg="red", command=self.back)

        self.menu.grid(row=2, column=1)

    def onselect(self, event):
        if (len(self.listbox.curselection()) >0):
            index = int(self.listbox.curselection()[0])
            print("sport : ", self._sports[index])
            self.delete_sport.grid(row=2, column=0, sticky = 'e', padx = 15 )
            self.current_sport = index
            self.yDefilCoach.grid(row=1, column=3, sticky='ns')
            self.listboxCoach.grid(row=1, column=2, sticky='nsew')
            self.titleCoachs.grid(row=0, column=2)

    def onselectCoachs(self, event):
        if (len(self.listboxCoach.curselection()) >0):
            indexCoach = int(self.listboxCoach.curselection()[0])
            indexSport = self.current_sport
            print("Coach :", self._sports[indexCoach])
            print("Sport :", self._sports[indexSport])
            self.assign_coach.grid(row=2, column=0, sticky = 'w', padx = 15 )
            self.delete_coach.grid(row=2, column=2, sticky = 'w', padx = 15 )

    def assign_coach(self):
        print("en attente")


    def show(self):
        self._sports = self._sport_controller.list_sports()
        self._coaches = self._person_controller.list_people(person_type='coach')
        self.listbox.delete(0, END)
        self.listboxCoach.delete(0, END)
        for index, sportctn in enumerate(self._sports):
            text = sportctn['name'].capitalize()
            self.listbox.insert(index, text)
        for index, sportctn in enumerate(self._coaches):
            text = sportctn['name'].capitalize()
            self.listboxCoach.insert(index, text)

        super().show()

    def delete_sport(self):
        index = int(self.listbox.curselection()[0])
        sport_id = self._sports[index]['id']
        self._sport_controller.delete_sport(sport_id)
        # show confirmation
        messagebox.showinfo("Success",
                            "Sport %s deleted !" % (self._sports[index]['name']))
        self.assign_coach.grid_forget()
        self.delete_sport.grid_forget()
        self.show()

    def delete_coach(self):
        print("en attente")