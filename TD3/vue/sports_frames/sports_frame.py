from tkinter import *
from tkinter import messagebox
from vue.sports_frames.add_sport_frame import AddSportFrame
from vue.sports_frames.sports_added_frame import SportsAddedFrame
from vue.base_frame import BaseFrame

class SportsFrame(BaseFrame):

    def __init__(self, member_controller, root_frame):
        super().__init__(root_frame)
        self._member_controller = member_controller
        self._create_widgets()
        self._members = None

    def _create_widgets(self):

        self.add_sports = Button(self, text="Add a sport", width=30,command=self.add_sport)
        self.sports_added = Button(self, text="Sports Added", width=30,command=self.sports_Added)
        self.menu = Button(self, text="Return", fg="red", command=self.show_menu)
        self.add_sports.pack()
        self.sports_added.pack()
        self.menu.pack()

    def add_sport(self):

        self.hide()
        add_sport_frame = AddSportFrame(self._member_controller, self) 
        self._root_frame._frames.append(add_sport_frame) 
        add_sport_frame.show() 

    def sports_Added(self):
          
        self.hide()
        sports_added_frame = SportsAddedFrame(self._member_controller, self) 
        self._root_frame._frames.append(sports_added_frame) 
        sports_added_frame.show() 