from argparse import *
from lib import *
from json import dumps


def parser_init() -> ArgumentParser:
    parser = ArgumentParser()
    sub_parser = parser.add_subparsers(dest='command')
    add_parser = sub_parser.add_parser('add')
    res_parser = sub_parser.add_parser('res')
    query_parser = sub_parser.add_parser('query')
    add_sub_parser = add_parser.add_subparsers(dest='target')
    add_flight_parser = add_sub_parser.add_parser('flight')
    add_flight_parser.add_argument('-f', '--flight-num', type=str, required=True, help='flight number',
                                   dest='flight_num')
    add_flight_parser.add_argument('-p', '--price', type=int, required=True, help='price', dest='price')
    add_flight_parser.add_argument('-s', '--seats', type=int, required=True, help='seats', dest='seats')
    add_flight_parser.add_argument('-o', '--origin', type=str, required=True, help='from city', dest='origin')
    add_flight_parser.add_argument('-a', '--ariv', type=str, required=True, help='arrive city', dest='ariv')

    add_bus_parser = add_sub_parser.add_parser('bus')
    add_bus_parser.add_argument('-l', '--location', type=str, required=True, help='location', dest='location')
    add_bus_parser.add_argument('-p', '--price', type=int, required=True, help='price', dest='price')
    add_bus_parser.add_argument('-s', '--seats', type=int, required=True, help='seats', dest='seats')

    add_hotel_parser = add_sub_parser.add_parser('hotel')
    add_hotel_parser.add_argument('-l', '--location', type=str, required=True, help='location', dest='location')
    add_hotel_parser.add_argument('-p', '--price', type=int, required=True, help='price', dest='price')
    add_hotel_parser.add_argument('-r', '--rooms', type=int, required=True, help='rooms', dest='rooms')

    add_customer_parser = add_sub_parser.add_parser('customer')
    add_customer_parser.add_argument('-n', '--name', type=str, required=True, help='name', dest='name')

    res_sub_parser = res_parser.add_subparsers(dest='target')
    res_flight_parser = res_sub_parser.add_parser('flight')
    res_flight_parser.add_argument('-n', '--name', type=str, required=True, help='name', dest='name')
    res_flight_parser.add_argument('-f', '--flight-num', type=str, required=True, help='flight number',
                                   dest='flight_num')

    res_hotel_parser = res_sub_parser.add_parser('hotel')
    res_hotel_parser.add_argument('-n', '--name', type=str, required=True, help='name', dest='name')
    res_hotel_parser.add_argument('-l', '--location', type=str, required=True, help='location', dest='location')

    res_bus_parser = res_sub_parser.add_parser('bus')
    res_bus_parser.add_argument('-n', '--name', type=str, required=True, help='name', dest='name')
    res_bus_parser.add_argument('-l', '--location', type=str, required=True, help='location', dest='location')

    query_sub_parser = query_parser.add_subparsers(dest='target')
    query_flight_parser = query_sub_parser.add_parser('flight')

    query_hotel_parser = query_sub_parser.add_parser('hotel')

    query_bus_parser = query_sub_parser.add_parser('bus')

    query_customer_parser = query_sub_parser.add_parser('customer')

    query_route_parser = query_sub_parser.add_parser('route')
    query_route_parser.add_argument('-n', '--name', type=str, required=True, help='name', dest='name')

    return parser


def parse(argv: list[str], cur: Cursor):
    parser = parser_init()
    args = parser.parse_args(argv)

    try:
        match args.command:
            case 'add':
                match args.target:
                    case 'flight':
                        add_flight(cur, args.flight_num, args.price, args.seats, args.origin, args.ariv)
                    case 'bus':
                        add_bus(cur, args.location, args.price, args.seats)
                    case 'hotel':
                        add_hotel(cur, args.location, args.price, args.rooms)
                    case 'customer':
                        add_customer(cur, args.name)
            case 'res':
                match args.target:
                    case 'flight':
                        apply_flight_res(cur, args.name, args.flight_num)
                    case 'bus':
                        apply_bus_res(cur, args.name, args.location)
                    case 'hotel':
                        apply_hotel_res(cur, args.name, args.location)
            case 'query':
                match args.target:
                    case 'flight':
                        result = list(map(lambda x: x.get_dict(), query_flights(cur)))
                        print(dumps(result))
                    case 'bus':
                        result = list(map(lambda x: x.get_dict(), query_buses(cur)))
                        print(dumps(result))
                    case 'hotel':
                        result = list(map(lambda x: x.get_dict(), query_hotels(cur)))
                        print(dumps(result))
                    case 'customer':
                        result = list(map(lambda x: x.get_dict(), query_customers(cur)))
                        print(dumps(result))
                    case 'route':
                        result = query_route(cur, args.name).get_dict()
                        print(dumps(result))

    except ValueError as e:
        print(e)
        return
    except Exception as e:
        print(e)
        return
