from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Client(Base):
    __tablename__ = "clients"
    client_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String)

    def __str__(self):
        return (f'client_id: {self.client_id}\n'
                f'first_name: {self.first_name}\n'
                f'last_name: {self.last_name}\n'
                f'email: {self.email}\n')

