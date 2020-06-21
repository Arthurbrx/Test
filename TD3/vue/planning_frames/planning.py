
from tkinter import *
from tkinter import messagebox
from vue.base_frame import BaseFrame


class PlanningFrame(BaseFrame):

    def __init__(self, planning_controller, root_frame):
        super().__init__(root_frame)
        self._planning_controller = planning_controller
        self._create_widgets()

    def _create_widgets(self):
        self.menu = Button(self, text="Return", fg="red", command=self.back)
        self.menu.grid(row=4, column=2, sticky=W)