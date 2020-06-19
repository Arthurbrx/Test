from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.sport import Sport
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound
from sqlalchemy.exc import SQLAlchemyError


class SportDAO(DAO):
    """
    Sports Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Sport).filter_by(id=id).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Sport).order_by(Sport.name).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_name(self, name: str):
        try:
            return self._database_session.query(Sport).filter_by(name=name).one()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        sport = Sport(name=data.get('name'), description=data.get('description'))
        self._database_session.add(sport)
        self._database_session.flush()
        return sport

    def update(self, sport: Sport, data: dict):
        if 'name' in data:
            sport.name = data['name']
        if 'description' in data:
            sport.description = data['description']
        try:
            self._database_session.merge(Sport)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Error data may be malformed")
        return Sport

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))
