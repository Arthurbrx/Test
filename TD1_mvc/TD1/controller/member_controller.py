import re

from model.dao.member_dao import MemberDAO
from exceptions import Error, InvalidData


class MemberController:
    """
    Member actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_members(self):
        # Permit to attribute the "Session" class to the new session 
        with self._database_engine.new_session() as session:
            members = MemberDAO(session).get_all()
            # To_dict is function  defined in model/mapping/member.py
            members_data = [member.to_dict() for member in members]
        return members_data
    def get_member(self, member_id):
        # TODO COntroller to get member
        return

    def create_member(self, data):
        # TODO COntroller to create a member
        return

    def update_member(self, member_id, member_data):
        # TODO Controller to update a member
        return

    def delete_member(self, member_id):
        # TODO Controller to delete a member
        return

    def search_member(self, firstname, lastname):
        # TODO Controller get a specific member
        return

    def _check_profile_data(self, data, update=False):
        name_pattern = re.compile("^[\S-]{2,50}$")
        email_pattern = re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
        mandatories = {
            'firstname': {"type": str, "regex": name_pattern},
            'lastname': {"type": str, "regex": name_pattern},
            'email': {"type": str, "regex": email_pattern}
        }
        for mandatory, specs in mandatories.items():
            if not update:
                if mandatory not in data or data[mandatory] is None:
                    raise InvalidData("Missing value %s" % mandatory)
            else:
                if mandatory not in data:
                    continue
            value = data[mandatory]
            if "type" in specs and not isinstance(value, specs["type"]):
                raise InvalidData("Invalid type %s" % mandatory)
            if "regex" in specs and isinstance(value, str) and not re.match(specs["regex"], value):
                raise InvalidData("Invalid value %s" % mandatory)
