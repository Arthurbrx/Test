from model.mapping import Base, generate_id
import uuid

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey

from model.mapping.person import Person


class Member(Person):
    __tablename__ = 'members'

    id = Column(String(36), ForeignKey('people.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'member',
    }
    def __repr__(self):
        return "<Member(%s %s)>" % (self.firstname, self.lastname.upper())

    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email
        }
