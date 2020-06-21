from sqlalchemy import UniqueConstraint, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from model.mapping import Base


class SportAssociation(Base):
    __tablename__ = 'sport_association'
    __table_args__ = (UniqueConstraint('person_id', 'sport_id'),)

    sport_id = Column(String(36), ForeignKey('sports.id'), primary_key=True)
    person_id = Column(String(36), ForeignKey('people.id'), primary_key=True)
    person = relationship("Person", back_populates="sports")
    sport = relationship("Sport", back_populates="people")