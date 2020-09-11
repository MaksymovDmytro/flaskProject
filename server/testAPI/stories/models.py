from sqlalchemy import Column, Integer, String
from testAPI.storage.repository import Base


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, nullable=False, unique=False)
    title = Column(String(200), nullable=False, unique=False)

    def serialize(self):
        return dict(
            id=self.id,
            userId=self.userId,
            title=self.title
        )
