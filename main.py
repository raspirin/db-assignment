#!/usr/bin/env python

import sys
from arg import *

if __name__ == '__main__':
    con = init()
    cur = con.cursor()
    # apply_bus_res(cur, "zhang3", "BEEF")
    # route = query_route(cur, "zhang3")
    # print(route)

    argv = sys.argv[1:]
    parse(argv, cur)
