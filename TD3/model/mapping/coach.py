from sqlalchemy import Column, String, ForeignKey
from model.mapping.person import Person


class Coach(Person):
    __tablename__ = 'coaches'

    id = Column(String(36), ForeignKey('people.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'coach',
    }

    def __repr__(self):
        return "<Coach(%s %s)>" % (self.firstname, self.lastname.upper())

    def to_dict(self):
        _dict = super().to_dict()
        return _dict
