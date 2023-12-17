from sqlite3 import Cursor, Connection
from ty import *
import sqlite3


def init() -> Connection:
    con = sqlite3.connect('database.db')
    con.execute("PRAGMA foreign_keys = ON;")
    con.commit()
    return con


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


# reservation
def apply_flight_res(cur: Cursor, name: str, flight_num: str):
    res = cur.execute("SELECT numAvail FROM FLIGHTS WHERE flightNum=?", (flight_num,))
    res = res.fetchone()
    if res is None:
        raise ValueError(f"No such flight: {flight_num}")
    num_avail = res[0]
    if num_avail == 0:
        raise ValueError("No available seat")

    cur.execute("UPDATE FLIGHTS SET numAvail=? WHERE flightNum=?", (num_avail - 1, flight_num))
    cur.execute("INSERT INTO RESERVATIONS (custName, resvType, resvKey) VALUES (?, ?, ?)", (name, 1, flight_num))
    commit(cur)


def apply_hotel_res(cur: Cursor, name: str, hotel_location: str):
    res = cur.execute("SELECT numAvail FROM HOTELS WHERE location=?", (hotel_location,))
    res = res.fetchone()
    if res is None:
        raise ValueError(f"No such hotel: {hotel_location}")
    num_avail = res[0]
    if num_avail == 0:
        raise ValueError("No available room")

    cur.execute("UPDATE HOTELS SET numAvail=? WHERE location=?", (num_avail - 1, hotel_location))
    cur.execute("INSERT INTO RESERVATIONS (custName, resvType, resvKey) VALUES (?, ?, ?)", (name, 2, hotel_location))
    commit(cur)


def apply_bus_res(cur: Cursor, name: str, bus_location: str):
    res = cur.execute("SELECT numAvail FROM BUS WHERE location=?", (bus_location,))
    res = res.fetchone()
    if res is None:
        raise ValueError(f"No such bus: {bus_location}")
    num_avail = res[0]
    if num_avail == 0:
        raise ValueError("No available seat")

    cur.execute("UPDATE BUS SET numAvail=? WHERE location=?", (num_avail - 1, bus_location))
    cur.execute("INSERT INTO RESERVATIONS (custName, resvType, resvKey) VALUES (?, ?, ?)", (name, 3, bus_location))
    commit(cur)


# query
def query_flights(cur: Cursor) -> [Flight]:
    res = cur.execute("SELECT * FROM FLIGHTS ORDER BY flightNum")
    res = res.fetchall()
    res = list(map(lambda x: Flight(x[0], x[1], x[2], x[3], x[4], x[5]), res))
    return res


def query_buses(cur: Cursor) -> [Bus]:
    res = cur.execute("SELECT * FROM BUS ORDER BY location").fetchall()
    res = list(map(lambda x: Bus(x[0], x[1], x[2], x[3]), res))
    return res


def query_hotels(cur: Cursor) -> [Hotel]:
    res = cur.execute("SELECT * FROM HOTELS ORDER BY location").fetchall()
    res = list(map(lambda x: Hotel(x[0], x[1], x[2], x[3]), res))
    return res


def query_customers(cur: Cursor) -> [Customer]:
    res = cur.execute("SELECT * FROM CUSTOMERS ORDER BY custName").fetchall()
    res = list(map(lambda x: Customer(x[0], x[1]), res))
    return res
