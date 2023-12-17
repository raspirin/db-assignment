from enum import IntEnum


class Flight:
    def __init__(self, flight_num, price, num_seats, num_avail, from_city, ariv_city):
        self.flight_num = flight_num
        self.price = price
        self.num_seats = num_seats
        self.num_avail = num_avail
        self.from_city = from_city
        self.ariv_city = ariv_city

    def __str__(self):
        return f"Flight {self.flight_num}: {self.from_city} to {self.ariv_city}, Price: {self.price}, Seats: {self.num_seats}, Available: {self.num_avail}"

    def get_dict(self):
        return {
            'flight_num': self.flight_num,
            'price': self.price,
            'num_seats': self.num_seats,
            'num_avail': self.num_avail,
            'from_city': self.from_city,
            'ariv_city': self.ariv_city
        }


class Bus:
    def __init__(self, location, price, num_bus, num_avail):
        self.location = location
        self.price = price
        self.num_bus = num_bus
        self.num_avail = num_avail

    def __str__(self):
        return f"Bus at {self.location}, Price: {self.price}, Buses: {self.num_bus}, Available: {self.num_avail}"

    def get_dict(self):
        return {
            'location': self.location,
            'price': self.price,
            'num_bus': self.num_bus,
            'num_avail': self.num_avail
        }


class Hotel:
    def __init__(self, location, price, num_rooms, num_avail):
        self.location = location
        self.price = price
        self.num_rooms = num_rooms
        self.num_avail = num_avail

    def __str__(self):
        return f"Hotel at {self.location}, Price: {self.price}, Rooms: {self.num_rooms}, Available: {self.num_avail}"

    def get_dict(self):
        return {
            'location': self.location,
            'price': self.price,
            'num_rooms': self.num_rooms,
            'num_avail': self.num_avail
        }


class Customer:
    def __init__(self, cust_name, cust_id):
        self.cust_name = cust_name
        self.cust_id = cust_id

    def __str__(self):
        return f"Customer {self.cust_name}, ID: {self.cust_id}"

    def get_dict(self):
        return {
            'cust_name': self.cust_name,
            'cust_id': self.cust_id
        }


class Route:
    def __init__(self):
        self.flight = None
        self.bus = None
        self.hotel = None

    def set_flight(self, flight):
        self.flight = flight

    def set_bus(self, bus):
        self.bus = bus

    def set_hotel(self, hotel):
        self.hotel = hotel

    def __str__(self):
        return f"Route: Flight: {self.flight}, Bus: {self.bus}, Hotel: {self.hotel}"

    def get_dict(self):
        return {
            'flight': None if self.flight is None else self.flight.get_dict(),
            'bus': None if self.bus is None else self.bus.get_dict(),
            'hotel': None if self.hotel is None else self.hotel.get_dict(),
        }


class ReservationTy(IntEnum):
    Flight = 1,
    Hotel = 2,
    Bus = 3,


class Reservation:
    def __init__(self, name: str, ty: ReservationTy, key: int):
        self.name = name
        self.ty = ty
        self.key = key

    def __str__(self):
        return f"Reservation: Customer: {self.name}, Type: {self.ty}, Key: {self.key}"
