import pymongo
from datetime import datetime
from .build_and_verify import build_and_verify_sample


class Client:
    def __init__(self, uri):
        """A mongodb client for RSoXS sample database.

        Parameters:
        -----------
        uri : a URI address of the mongo database in a format
              'mongodb://localhost:27017/test-rsoxs-database'
        """

        self.uri = uri
        self.database = _get_database(uri)

    def new_sample(self, *, sample_name='test', sample_desc='testing',
                   date_created=datetime.now().strftime('%G-%m-%d-%I:%M:%S %p'),
                   user_id=0, project_name='testing', institution_id=0,
                   composition=[], density=1, thickness=1, notes='',
                   state='fresh', current_bar_id=0, current_slot_name='blank',
                   past_bar_ids=[], location_id=0, requests=[], history=[],
                   priority=0):
        # We could have used **kwargs, but we decided to repeat all the kwargs
        # for the users to see the expected signature when using 'help()' or '?'.
        sample = build_and_verify_sample(sample_name=sample_name,
                                         sample_desc=sample_desc,
                                         date_created=date_created,
                                         user_id=user_id,
                                         project_name=project_name,
                                         institution_id=institution_id,
                                         composition=composition,
                                         density=density,
                                         thickness=thickness,
                                         notes=notes,
                                         state=state,
                                         current_bar_id=current_bar_id,
                                         current_slot_name=current_slot_name,
                                         past_bar_ids=past_bar_ids,
                                         location_id=location_id,
                                         requests=requests, history=history,
                                         priority=priority)
        return self.database.samples.insert_one(sample)

    def find_samples(self, query):
        return self.database.samples.find(query)


def _get_database(uri):
    client = pymongo.MongoClient(uri)
    try:
        # Called with no args, get_database() returns the database
        # specified in the client's uri --- or raises if there was none.
        # There is no public method for checking this in advance, so we
        # just catch the error.
        return client.get_database()
    except pymongo.errors.ConfigurationError as err:
        raise ValueError(
            f"Invalid client: {client} "
            f"Did you forget to include a database?") from err
        
