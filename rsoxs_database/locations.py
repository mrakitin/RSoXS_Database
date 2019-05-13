
def goto_location(location_id):
    loc_dict = dict_from_key("location",location_id)
    loc_list = [].append(loc_dict['location_list'])
    mots = [d['motor'] for d in loc_list if 'motor' in d]
    sps = [d['setpoint'] for d in loc_list if 'setpoint' in d]
    order = [d['order'] for d in loc_list if 'order' in d]


