from model.dao.member_dao import MemberDAO
from model.mapping.person import Person
from model.dao.dao import DAO
from model.dao.member_dao import MemberDAO
from model.dao.coach_dao import CoachDAO

class PersonDAO(DAO):
    """
    Person Mapping DAO
    """

    def __init__(self, database_session, person_type=Person):
        super().__init__(database_session)
        self._person_type = person_type

    def get(self, id):
        return self._database_session.query(self._person_type).filter_by(id=id).one()

    def get_all(self):
        return self._database_session.query(self._person_type).order_by(self._person_type.firstname).all()

    def get_by_name(self, firstname: str, lastname: str):
        return self._database_session.query(self._person_type)\
            .filter_by(firstname=firstname, lastname=lastname).one()

    def _update_address(self, member, address_data):
        if member.address is not None:
            if 'street' in address_data:
                member.address.street = address_data['street']
            if 'postal_code' in address_data:
                member.address.postal_code = address_data['postal_code']
            if 'city' in address_data:
                member.address.city = address_data['city']
            if 'country' in address_data:
                member.address.country = address_data['country']
        else:
            member.set_address(address_data['street'], address_data['postal_code'], address_data['city'],
                               address_data.get('country', 'FRANCE'))

    def update(self, member: Person, data: dict):
        if 'firstname' in data:
            member.firstname = data['firstname']
        if 'lastname' in data:
            member.lastname = data['lastname']
        if 'email' in data:
            member.email = data['email']
        if 'address' in data:
            self._update_address(member, data['address'])

        self._database_session.merge(member)
        self._database_session.flush()
        return member

    def delete(self, entity):
        self._database_session.delete(entity)

    def get_dao(self, type=None):
        if type is None:
            return PersonDAO(self._database_session)

        if type == 'member':
            return MemberDAO(self._database_session)
        elif type == 'coach':
            return CoachDAO(self._database_session)
        else:
            return PersonDAO(self._database_session)