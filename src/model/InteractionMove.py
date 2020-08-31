import datetime
import uuid

from sqlalchemy import Boolean, DateTime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from concrete.artifacts.Artifact import Artifact
from helpers.Constants import *
from settings.db_settings import Base


class InteractionMove(Base):

    __tablename__ = 'InteractionMove'

    playerName = Column(String(100))
    id = Column(String(36), primary_key=True)
    relativeId = Column(Integer)
    moveName = Column(String(100))
    artifact = Column(String(100))
    role = Column(String(100))
    final = Column(Boolean)
    dateCreated = Column(DateTime)

    def __init__(self, id: str = None, relativeId: int = None, moveName: str = EMPTY, artifact: str = EMPTY,
                 playerName: str = EMPTY, role: str = EMPTY, final: bool = False):
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.moveName = moveName
        self.relativeId = relativeId
        if isinstance(artifact, Artifact):
            self.artifact = artifact
        else:
            self.artifact = Artifact(artifact)
        self.playerName = playerName
        self.role = role
        self.final = final
        self.dateCreated = datetime.datetime.utcnow()
