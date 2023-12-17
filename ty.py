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


class Bus:
    def __init__(self, location, price, num_bus, num_avail):
        self.location = location
        self.price = price
        self.num_bus = num_bus
        self.num_avail = num_avail

    def __str__(self):
        return f"Bus at {self.location}, Price: {self.price}, Buses: {self.num_bus}, Available: {self.num_avail}"


class Hotel:
    def __init__(self, location, price, num_rooms, num_avail):
        self.location = location
        self.price = price
        self.num_rooms = num_rooms
        self.num_avail = num_avail

    def __str__(self):
        return f"Hotel at {self.location}, Price: {self.price}, Rooms: {self.num_rooms}, Available: {self.num_avail}"


class Customer:
    def __init__(self, cust_name, cust_id):
        self.cust_name = cust_name
        self.cust_id = cust_id

    def __str__(self):
        return f"Customer {self.cust_name}, ID: {self.cust_id}"
