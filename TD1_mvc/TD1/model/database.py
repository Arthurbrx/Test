
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.mapping import Base

# See slqalchemy from more information. 
# Sqlalchemy use a system of session to manipulate the created database. 
# To use it, have to initiate a new session and commit your changements to use it. 
# The Session class is here to automatically do the commit or rollback functions.
# You are free to use it or not, but don't forget to commit, flush or rollback ;) 


#The databse class is here to have the basics database functions
class DatabaseEngine:
    """
    Database Engine
    Handle Database connections and sessions
    """

    def __init__(self, url='sqlite:///:memory:', verbose=False):
        self._engine = create_engine(url, echo=verbose)
        self._Session = sessionmaker(bind=self._engine)

    def new_session(self):
        sqlalchemy_session = self._Session()
        return Session(sqlalchemy_session)

    def create_database(self):
        Base.metadata.create_all(self._engine)

    def remove_database(self):
        Base.metadata.drop_all(self._engine)


class Session:

    def __init__(self, sql_alchemy_session, autocommit=True):
        self._session = sql_alchemy_session
        self._autocommit = autocommit

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._autocommit:
            if exc_type is not None:
                self._session.rollback()
            else:
                self._session.commit()
        self._session.close()
        return False

    def add(self, entity):
        self._session.add(entity)

    def query(self, *entity_class):
        return self._session.query(*entity_class)

    def merge(self, entity):
        return self._session.merge(entity)

    def delete(self, entity):
        self._session.delete(entity)

    def flush(self):
        self._session.flush()

    def commit(self):
        self._session.commit()

    def close(self):
        self._session.close()
