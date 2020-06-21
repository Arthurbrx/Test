from model.mapping import Base
import uuid
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, UniqueConstraint


class Sport(Base):
    __tablename__ = 'sports'

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    name = Column(String(50), nullable=False, unique=True)
    people = relationship("SportAssociation", back_populates="sport")

    def __repr__(self):
        return "<Sport %s>" % self.name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }
