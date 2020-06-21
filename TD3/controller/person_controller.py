import re
import logging

from model.dao.sport_dao import SportDAO

from exceptions import Error, InvalidData
from model.dao.person_dao import PersonDAO


class PersonController:
    """
    Member actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def list_people(self, person_type=None):
        with self._database_engine.new_session() as session:
            people = PersonDAO(session).get_dao(type=person_type).get_all()
            people_data = [member.to_dict() for member in people]
        return people_data

    def get_person(self, person_id, person_type=None):
        with self._database_engine.new_session() as session:
            member = PersonDAO(session).get_dao(type=person_type).get(person_id)
            member_data = member.to_dict()
        return member_data

    def get_member(self, member_id):
        return self.get_person(member_id, person_type='member')

    def create_person(self, data, person_type=None):
        self._check_person_data(data)
        try:
            with self._database_engine.new_session() as session:
                member = PersonDAO(session).get_dao(type=person_type).create(data)
                member_data = member.to_dict()
                return member_data
        except Error as e:
            raise e

    def create_member(self, data):
        return self.create_person(data, 'member')

    def create_coach(self, data):
        return self.create_person(data, 'coach')

    def _update_person(self, member_id, member_data, person_type=None):
        with self._database_engine.new_session() as session:
            person = PersonDAO(session).get_dao(type=person_type).get(member_id)
            person = PersonDAO(session).get_dao(type=person_type).update(person, member_data)
            return person.to_dict()

    def update_person(self, member_id, member_data):
        self._check_person_data(member_data, update=True)
        return self._update_person(member_id, member_data, person_type='person')

    def update_member(self, member_id, data):
        self._check_member_data(data, update=True)
        return self._update_person(member_id, data, person_type='member')

    def update_coach(self, member_id, data):
        self._check_coach_data(data, update=True)
        return self._update_person(member_id, data, person_type='coach')

    def delete_person(self, member_id, person_type=None):
        with self._database_engine.new_session() as session:
            dao = PersonDAO(session).get_dao(type=person_type)
            member = dao.get(member_id)
            dao.delete(member)

    def search_person(self, firstname, lastname, person_type=None):
        # Query database
        with self._database_engine.new_session() as session:
            dao = PersonDAO(session).get_dao(type=person_type)
            member = dao.get_by_name(firstname, lastname)
            return member.to_dict()

    def _check_member_data(self, data, update=False):
        self._check_person_data(data, update=update)
        specs = {
            'medical_certificate': {"type": bool},
        }
        self._check_data(data, specs, update=update)

    def _check_coach_data(self, data, update=False):
        self._check_person_data(data, update=update)
        specs = {
            'degree': {"type": str},
            'certificate': {"type": str}
        }
        self._check_data(data, specs, update=update)

    def _check_person_data(self, data, update=False):
        name_pattern = re.compile("^[\S-]{2,50}$")
        email_pattern = re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
        specs = {
            'firstname': {"type": str, "regex": name_pattern},
            'lastname': {"type": str, "regex": name_pattern},
            'email': {"type": str, "regex": email_pattern}
        }
        self._check_data(data, specs, update=update)

        if 'address' in data:
            address = data['address']
            specs = {
                'street': {"type": str},
                'postal_code': {"type": int},
                'city': {"type": str}
            }
            self._check_data(address, specs, update=update)

    def _check_data(self, data, specs, update=False):
        for mandatory, specs in specs.items():
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