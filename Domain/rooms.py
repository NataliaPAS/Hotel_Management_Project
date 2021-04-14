from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean

Base = declarative_base()


class Rooms(Base):
    __tablename__ = "rooms"
    room_number = Column(Integer, primary_key=True)
    room_type = Column(String, nullable=False)
    price_per_night = Column(Float, nullable=False)
    size_room = Column(Integer, nullable=False)
    has_view = Column(Boolean, nullable=False)

    def __str__(self):
        return (f'room_number: {self.room_number}\n'
                f'room_type: {self.room_type}\n'
                f'price_per_night: {self.price_per_night}\n'
                f'size_room: {self.size_room}\n'
                f'has_view: {self.has_view}\n')

