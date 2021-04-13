from sqlalchemy import create_engine, text
import datetime

from Domain.clients import Client
from Domain.rooms import Rooms

engine = create_engine('mysql+pymysql://root:@localhost:3306/Hotel_Management', echo=False)

room_type = ["Double room", "Superior Double room", "Deluxe Double room", "Suite", "Deluxe suite", "Presidential Suite"]

if __name__ == '__main__':
    all_clients = []
    with engine.connect() as conn:
        query = conn.execute(text('SELECT * FROM clients'))
        for item in query:
            client = Client(
                cnp=item[0],
                first_name=item[1],
                last_name=item[2],
                email=item[3],
                city=item[4]
            )
            all_clients.append(client)
    print(all_clients)
    rooms = []
    with engine.connect() as conn:
        query = conn.execute(text('SELECT * FROM rooms'))
        for item in query:
            rooms = Rooms(
                room_number=item[0],
                room_type=item[1],
                price_per_night=item[2],
                size_room=item[3],
                has_view=item[4]
            )
            rooms.append(rooms)
    print(rooms)

