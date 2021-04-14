from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, Date
from clients import Client
from rooms import Rooms

Base = declarative_base()


class Reservations(Base):
    __tablename__ = "reservations"
    reservation_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey(Client.client_id), nullable=False)
    room_number = Column(Integer, ForeignKey(Rooms.room_number), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    def __str__(self):
        return (f'client_id: {self.client_id}\n'
                f'room_number: {self.room_number}\n'
                f'start_date: {self.start_date}\n'
                f'end_date: {self.end_date}\n')

