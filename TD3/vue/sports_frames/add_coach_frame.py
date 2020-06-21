
from tkinter import *
from tkinter import messagebox
from vue.base_frame import BaseFrame


class AddCoachFrame(BaseFrame):

    def __init__(self, person_controller, root_frame):
        super().__init__(root_frame)
        self._person_controller = person_controller
        self.name_pattern = re.compile("^[\S-]{2,50}$")
        self._create_widgets()

    def _create_widgets(self):

        self.name_entry = self.create_entry("Add a coach", row=0, validate_callback=self.validate_name)
        self.valid = Button(self, text="Valid", fg="red", command=self.valid)
        self.valid.grid(row=4, column=1, sticky=E)
        self.menu = Button(self, text="Return", fg="red", command=self.back)
        self.menu.grid(row=4, column=2, sticky=W)

    def validate_name(self, event, entry=None):

        if not self.name_pattern.match(entry.get()):
            entry.config(fg='red')
        else:
            entry.config(fg='black')

    def valid(self): # a changer

        data = dict(name=self.name_entry.get())
        print (data)
        try:
            sport_data = self._person_controller.create_coach(data)
            messagebox.showinfo("Success","Coach %s created !" % (sport_data['Firstname']))

        except Error as e:
            messagebox.showerror("Error", str(e))
            return

        self.back()
