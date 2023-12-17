from lib import *

con = init()
cur = con.cursor()
# apply_bus_res(cur, "zhang3", "BEEF")
route = query_route(cur, "zhang3")
print(route)