from model.database import DatabaseEngine
from controller.person_controller import PersonController
from model.dao.sport_dao import SportDAO

from controller.sport_controller import SportController

from vue.root_frame import RootFrame


def main():
    print("Welcome in BDS App")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///bds.db')
    database_engine.create_database()


    # controller
    person_controller = PersonController(database_engine)
    sport_controller = SportController(database_engine)
    planning_controller = SportController(database_engine) #a changer

    # init vue
    root = RootFrame(person_controller, sport_controller, planning_controller)
    root.master.title("bds subscription app")
    root.show_menu()

    # start
    root.mainloop()


if __name__ == "__main__":
    main()
