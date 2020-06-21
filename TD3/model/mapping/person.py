from model.mapping import Base, generate_id
import uuid

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from model.mapping.sport_association import SportAssociation
from exceptions import ResourceNotFound


class Person(Base):
    __tablename__ = 'people'
    __table_args__ = (UniqueConstraint('firstname', 'lastname'),)

    id = Column(String(36), default=generate_id, primary_key=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(256), nullable=False)
    person_type = Column(String(50), nullable=False)
    sports = relationship("SportAssociation", back_populates="person")

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': person_type
    }

    def __repr__(self):
        return "<Person(%s %s)>" % (self.firstname, self.lastname.upper())

    def to_dict(self):
        _data = {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "sports": []
        }
        for sport_association in self.sports:
            _data['sports'].append({"level": sport_association.level,
                                    "id": sport_association.sport.id,
                                    "name": sport_association.sport.name})

        return _data