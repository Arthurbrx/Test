
import sys
from vue.member_vue import MemberVue
from exceptions import ResourceNotFound, Error, InvalidData


class AdminVue(MemberVue):
    """
    Admin Vue
    Admin specific interfaces
    """

    def __init__(self, member_controller):
        super().__init__(member_controller)

    def help(self, commands):
        print()
        for command, description in commands.items():
            print("  * %s: '%s'" % (command, description))
        print()

    def ask_command(self, commands):

        command = input('command > ').lower().strip()
        while command not in commands.keys():
            print("Unknown command")
            command = input('command >').lower().strip()

        return command


    def admin_shell(self):
        # TODO to choose your action
        commands = {
            "exit": "Quit the Shell",
            "add": "Add association member",
            "list": "List association members",
            "search": "Show member profile",
            "delete": "Delete a member",
            "update": "Update a member",
            "help": "Show this help"
        }

        self.help(commands)

        while True:
            try:
                command = self.ask_command(commands)
                if command == 'exit':
                    # Exit loop
                    break
                elif command == 'add':
                    # TODO
                    continue
                elif command == 'list':
                    self.show_members()
                elif command == 'search':
                    # TODO
                    continue
                elif command == 'delete':
                    # TODO
                    continue
                elif command == 'update':
                    # TODO
                    continue
                elif command == 'help':
                    # TODO
                    continue
                else:
                    print("Unknown command")
            except ResourceNotFound:
                self.error_message("Member not found")
            except InvalidData as e:
                self.error_message(str(e))
            except Error as e:
                self.error_message("An error occurred (%s)" % str(e))
