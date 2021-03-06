from tkinter import Label, Button
from vue.base_frame import BaseFrame


class MemberMenuFrame(BaseFrame):
    def __init__(self, root_frame):
        super().__init__(root_frame)
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(self, text="Welcome in BDS App")
        self.subscribe = Button(self, text="Subscribe", width=30, command=self._root_frame.show_subscribe)
        self.list = Button(self, text="List members", width=30, command=self._root_frame.show_members)
        self.sports = Button(self, text="Sports", width=30,command=self._root_frame.show_sports)
        self.planning = Button(self, text="Scheduling", width=30,command=self._root_frame.show_planning)
        self.quit = Button(self, text="QUIT", fg="red", width=30, command=self.quit)
        self.title.pack(side="top")
        self.subscribe.pack()
        self.list.pack()
        self.sports.pack()
        self.planning.pack()
        self.quit.pack(side="bottom")
