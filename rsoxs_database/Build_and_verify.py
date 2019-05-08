import jsonschema


def build_and_verify_user(date_list,email, first_name, institution_id, last_checkin, last_name, notes,
                          past_institutions,past_proposals, phone, proposal_id, user_id, username, history):

    user = {'date_checkin_list': date_list,
            'email': email,
            'first_name': first_name,
            'institution_id': institution_id,
            'last_checkin': last_checkin,
            'last_name': last_name,
            'notes': notes,
            'past_institutions': past_institutions,
            'past_proposals': past_proposals,
            'phone': phone,
            'proposal_id': proposal_id,
            'user_id': user_id,
            'username': username,
            'history': history}

    jsonschema.validate(user,{'$ref': 'file:/Users/greateyes/.ipython/profile_collection/startup/schema/'
                                      'RSoXS_User.json'})
    return user


def build_and_verify_sample(sample_name, sample_desc, date_created, user_id, project_name, institution_id,
                            composition, density, thickness, notes, state, current_bar_id, current_slot_name,
                            past_bar_ids, location_id, collections, history):
    sample = {"sample_name": sample_name,
              "sample_desc": sample_desc,
              "date_created": date_created,
              "user_id": user_id,
              "project_name": project_name,
              "institution_id": institution_id,
              "composition": composition,
              "density": density,
              "thickness": thickness,
              "notes": notes,
              "state": state,
              "current_bar_id": current_bar_id,
              "current_slot_name": current_slot_name,
              "past_bar_ids": past_bar_ids,
              "location_id": location_id,
              "collections": collections,
              "history": history
              }

    jsonschema.validate(sample,{'$ref': 'file:/Users/greateyes/.ipython/profile_collection/startup/schema/'
                                        'RSoXS_Sample.json'})
    return sample


def build_and_verify_location(location_list,display, favorite, creator_id, sample, config):

    location = {"location_list": location_list,
                "display": display,
                "favorite": favorite,
                "creator_ID": creator_id,
                "sample": sample,
                "config": config
                }

    jsonschema.validate(location,{'$ref': 'file:/Users/greateyes/.ipython/profile_collection/startup/schema/'
                                          'RSoXS_Location.json'})
    return location


def build_and_verify_institution(institution_id, full_name, short_name, notes):

    institution = {
        "institution_id": institution_id,
        "full_name": full_name,
        "short_name": short_name,
        "notes": notes
    }

    jsonschema.validate(institution,{'$ref': 'file:/Users/greateyes/.ipython/profile_collection/startup/schema/'
                                             'RSoXS_Institution.json'})
    return institution


def build_and_verify_holder(holder_id,holder_name, primary_user_id, primary_institution_id, primary_proposal_id,
                            date_loaded_list, notes, slots, history):

    holder = {
        "holder_id": holder_id,
        "holder_name": holder_name,
        "primary_user_id": primary_user_id,
        "primary_institution_id": primary_institution_id,
        "primary_proposal_id": primary_proposal_id,
        "date_loaded_list": date_loaded_list,
        "notes": notes,
        "slots": slots,
        'history': history
    }

    jsonschema.validate(holder,{'$ref': 'file:/Users/greateyes/.ipython/profile_collection/startup/schema/'
                                        'RSoXS_Holder.json'})
    return holder


def build_and_verify_configuration(plan_name,motors, positions, display, favorite, creator_ID):

    configuration = {
        "plan_name": plan_name,
        "motors": motors,
        "positions": positions,
        "display": display,
        "favorite": favorite,
        "creator_ID": creator_ID,
    }

    jsonschema.validate(configuration,{'$ref': 'file:/Users/greateyes/.ipython/profile_collection/startup/schema/'
                                               'RSoXS_Configuration.json'})
    return configuration


def build_and_verify_acquisition(plan_name,detectors, motors, positions, display, favorite, creator_ID):

    acquisition = {
        "plan_name": plan_name,
        "detectors": detectors,
        "motors": motors,
        "positions": positions,
        "display": display,
        "favorite": favorite,
        "creator_ID": creator_ID
    }

    jsonschema.validate(acquisition,{'$ref': 'file:/Users/greateyes/.ipython/profile_collection/startup/schema/'
                                             'RSoXS_Acquisition.json'})
    return acquisition
