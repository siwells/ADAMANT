import sqlalchemy
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from settings.db_settings import Base


class DatabaseController:
    def __init__(self, engine: Engine = None):
        if engine is None:
            self.__engine = sqlalchemy.create_engine('sqlite:///database_adamantium.sqlite')
        else:
            self.__engine = engine
        session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.__engine))
        Base.query = session.query_property()
        import model
        Base.metadata.create_all(bind=self.__engine)
        self.__session = session()

    def __set_engine(self, engine: Engine):
        self.__engine = engine

    def __get_engine(self) -> Engine:
        return self.__engine

    def __set_session(self, session: Session):
        self.__session = session

    def __get_session(self) -> Session:
        return self.__session

    engine = property(__get_engine, __set_engine, None)
    session = property(__get_session, __set_session, None)
