from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"
    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    occupation = Column(String, nullable=False)

    def __str__(self):
        return (f'employee_id: {self.employee_id}\n'
                f'first_name: {self.first_name}\n'
                f'last_name: {self.last_name}\n'
                f'occupation: {self.occupation}\n')

