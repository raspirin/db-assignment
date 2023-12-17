from lib import *

con = init()
cur = con.cursor()
apply_flight_res(cur, "zhang3", "asdf")
# apply_bus_res(cur, "zhang3", "BEEF")