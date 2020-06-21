from model.mapping.coach import Coach
from model.dao.person_dao import PersonDAO


class CoachDAO(PersonDAO):
    """
    Coach Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session, person_type=Coach)

    def create(self, data: dict):
        coach = Coach(firstname=data.get('firstname'), lastname=data.get('lastname'), email=data.get('email'))
        self._database_session.add(coach)
        self._database_session.flush()
        return coach

    def update(self, coach: Coach, data: dict):
        super().update(coach, data)
        self._database_session.merge(coach)
        self._database_session.flush()
        return coach
