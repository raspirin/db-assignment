from lib import *

con = init()
cur = con.cursor()
# apply_bus_res(cur, "zhang3", "BEEF")
flights = query_flights(cur)
buses = query_buses(cur)
hotels = query_hotels(cur)
customers = query_customers(cur)
