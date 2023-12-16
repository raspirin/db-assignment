from sqlite3 import Cursor


# utils
def commit(cur: Cursor):
    cur.connection.commit()


# adding
def add_flight(cur: Cursor, flight_num: str, price: int, num_seats: int, from_city: str, ariv_city: str):
    data = (flight_num, price, num_seats, num_seats, from_city, ariv_city)
    cur.execute("INSERT INTO FLIGHTS VALUES (?, ?, ?, ?, ?, ?)", data)
    commit(cur)


def add_bus(cur: Cursor, location: str, price: int, num_seats: int):
    data = (location, price, num_seats, num_seats)
    cur.execute("INSERT INTO BUS VALUES (?, ?, ?, ?)", data)
    commit(cur)


def add_hotel(cur: Cursor, location: str, price: int, num_rooms: int):
    data = (location, price, num_rooms, num_rooms)
    cur.execute("INSERT INTO HOTELS VALUES (?, ?, ?, ?)", data)
    commit(cur)


def add_customer(cur: Cursor, name: str):
    id = hash(name)
    data = (name, id)
    cur.execute("INSERT INTO CUSTOMERS VALUES (?, ?)", data)
    commit(cur)
