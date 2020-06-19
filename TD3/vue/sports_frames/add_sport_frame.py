
from tkinter import *
from tkinter import messagebox
from vue.base_frame import BaseFrame


class AddSportFrame(BaseFrame):

    def __init__(self, member_controller, root_frame):
        super().__init__(root_frame)
        self._member_controller = member_controller
        self.name_pattern = re.compile("^[\S-]{2,50}$")
        self._create_widgets()
        self._members = None

    def _create_widgets(self):

        self.firstname_entry = self.create_entry("Add a sport", row=0, validate_callback=self.validate_name)
        self.valid = Button(self, text="Valid", fg="red", command=None)
        self.valid.grid(row=4, column=1, sticky=E)
        self.menu = Button(self, text="Return", fg="red", command=self.back)
        self.menu.grid(row=4, column=2, sticky=W)

    def validate_name(self, event, entry=None):

        if not self.name_pattern.match(entry.get()):
            entry.config(fg='red')
        else:
            entry.config(fg='black')