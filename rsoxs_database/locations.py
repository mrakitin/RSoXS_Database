
from operator import attrgetter
import collections


def goto_location(loc_dict):
    loc_list = [].append(loc_dict['location_list'])
    loc_list = sorted(loc_list,key=attrgetter('order'))
    orderlist = [o for o in collections.Counter(d['order'] for d in loc_list).keys()]
    for order in orderlist:
        outputlist = [[items['motor'], items['position']] for items in loc_list if items['order'] == order]
        flat_list = [item for sublist in outputlist for item in sublist]
        yield from bps.mv(*flat_list)






