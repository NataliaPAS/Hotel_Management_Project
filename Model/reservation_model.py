
from sqlalchemy.orm import sessionmaker
from Domain.reservations import Reservations
from datetime import datetime


class ReservationSQLModel:

    def __init__(self, engine):
        self.__engine = engine
        self.__my_session = sessionmaker(bind=engine)()

    def create_reservation(self, client_id, room_number, start_date, end_date):
        self.__my_session.add(Reservations(client_id=client_id, room_number=room_number,start_date=start_date, end_date=end_date))
        self.__my_session.commit()

    def read_reservation(self):
        return self.__my_session.query(Reservations).all()

    def update_reservation(self, reservation_id, client_id=None, room_number=None, start_date=None, end_date=None):
        my_reservation = self.__my_session.query(Reservations).filter_by(reservation_id=reservation_id).first()
        if my_reservation:
            self.__my_session.query(Reservations).filter_by(reservation_id=reservation_id).update({
                "client_id": f"{client_id or my_reservation.client_id}",
                "room_number": f"{room_number or my_reservation.room_number}",
                "start_date": f"{start_date or my_reservation.start_date}",
                "end_date": f"{end_date or my_reservation.end_date}",
            })
            self.__my_session.commit()

    def delete_reservation(self, reservation_id):
        self.__my_session.query(Reservations).filter_by(reservation_id=reservation_id).delete()
        self.__my_session.commit()

    def find_by_reservation_id(self, reservation_id):
        my_reservation = self.__my_session.query(Reservations).filter_by(reservation_id=reservation_id).first()
        return my_reservation

    def reservation_id_exists(self, reservation_id):
        my_reservation = self.__my_session.query(Reservations).filter_by(reservation_id=reservation_id).first()
        return True if my_reservation else False

    def get_reservations_start_date_today(self, start_date=datetime.today()):
        my_reservation = self.__my_session.query(Reservations).filter_by(start_date=datetime.today()).all()
        return my_reservation

    def get_reservations_end_date_today(self, end_date):
        my_reservation = self.__my_session.query(Reservations).filter_by(end_date=datetime.today()).all()
        return my_reservation

    def get_last_reservation_id(self):
        my_reservation = self.__my_session.query(Reservations).order_by(Reservations.reservation_id.desc()).first()
        return my_reservation.reservation_id


if __name__ == "__main__":
    from sqlalchemy import create_engine

    engine = create_engine('mysql+pymysql://root:@localhost:3306/Hotel_Management', echo=False)
    model = ReservationSQLModel(engine=engine)

    for reservation in model.get_reservations_start_date_today(start_date=datetime.today()):
        print(reservation)

    for reservation in model.get_reservations_end_date_today(end_date=datetime.today()):
        print(reservation)



    # model.create_reservation(client_id=321, room_number=13, start_date='20/04/21', end_date='22/04/21')
    # model.update_reservation(reservation_id=model.get_last_reservation_id, client_id=123, room_number=7, start_date='20/05/21', end_date='23/05/21')
    # for reservation in model.read_reservation():
    #     print(reservation)

    # model.delete_reservation(123)
