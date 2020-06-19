from vue.common import Common


class MemberVue:
    """
    Member Vue
    Members interface features
    """

    def __init__(self, member_controller):
        self._common = Common()
        self._member_controller = member_controller

    def add_member(self):
        # Show subscription formular
        # TODO Formular to add a member (asking name... and send it to controller)
        return
       

    def show_member(self, member: dict):
        print("Member profile: ")
        print(member['firstname'].capitalize(), member['lastname'].capitalize())
        print("email:", member['email'])

    def error_message(self, message: str):
        print("/!\\ %s" % message.upper())

    def succes_message(self, message: str = ""):
        print("Operation succeeded: %s" % message)

    def show_members(self):
        members = self._member_controller.list_members()

        print("Members: ")
        for member in members:
            print("* %s %s (%s)" % (member['firstname'].capitalize(),
                                    member['lastname'].capitalize(),
                                    member['email']))

        return
       

    def search_member(self):
        # TODO Find a member with firstname and name
        return

    def update_member(self):
        # TODO Change a member name or firstname
        return

    def delete_member(self):
        # TODO Delete a member
        return
