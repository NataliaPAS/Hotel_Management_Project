from sqlalchemy.orm import sessionmaker
from Domain.employees import Employee


class EmployeeSQLModel:

    def __init__(self, engine):
        self.__engine = engine
        self.__my_session = sessionmaker(bind=engine)()

    def create_employee(self, employee_id, first_name, last_name, occupation):
        self.__my_session.add(Employee(employee_id=employee_id, first_name=first_name, last_name=last_name, occupation=occupation))
        self.__my_session.commit()

    def read_employee(self):
        return self.__my_session.query(Employee).all()

    def update_employee(self, employee_id, first_name=None, last_name=None, occupation=None):
        my_employee = self.__my_session.query(Employee).filter_by(employee_id=employee_id).first()
        if my_employee:
            self.__my_session.query(Employee).filter_by(employee_id=employee_id).update({
                "first_name": f"{first_name or my_employee.first_name}",
                "last_name": f"{last_name or my_employee.last_name}",
                "occupation": f"{occupation or my_employee.occupation}",
            })
            self.__my_session.commit()

    def delete_employee(self, employee_id):
        self.__my_session.query(Employee).filter_by(employee_id=employee_id).delete()
        self.__my_session.commit()

    def find_by_employee_id(self, employee_id):
        my_employee = self.__my_session.query(Employee).filter_by(employee_id=employee_id).first()
        return my_employee

    def employee_id_exists(self, employee_id):
        my_employee = self.__my_session.query(Employee).filter_by(employee_id=employee_id).first()
        return True if my_employee else False


if __name__ == "__main__":
    from sqlalchemy import create_engine

    engine = create_engine('mysql+pymysql://root:@localhost:3306/Hotel_Management', echo=False)
    model = EmployeeSQLModel(engine=engine)

    model.create_employee(4569, "employee1", "test", "receptionist")
    model.update_employee(4569, "employee2", "test2", "receptionist")

    for employee in model.read_employee():
        print(employee)

    # model.delete_employee(4569)
