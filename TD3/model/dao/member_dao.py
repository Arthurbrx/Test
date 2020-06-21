from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.member import Member
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound
from sqlalchemy.exc import SQLAlchemyError


class MemberDAO(DAO):
    """
    Member Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def create(self, data: dict):
        try:
            member = Member(firstname=data.get('firstname'), lastname=data.get('lastname'), email=data.get('email'))
            print(member.to_dict())
            self._database_session.add(member)
            self._database_session.flush()
        except IntegrityError as e:
            print(e)
            raise Error("Member already exists")
        return member

    def update(self, member: Member, data: dict):
        super().update(member, data)
        self._database_session.merge(member)
        self._database_session.flush()
        return member


