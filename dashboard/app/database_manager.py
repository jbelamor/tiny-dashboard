import pymongo
import config

class DB(object):
    def get_database():
        client = pymongo.MongoClient(config.mongoURL)
        return(client[config.db_name])

    @staticmethod
    def get_all_data_collection(collection, filter_={}, exclude={}):
        database = DB.get_database()
        elements = database[collection].find(filter_, exclude)
        return(elements)

    @staticmethod
    def get_one_elem(collection, elem_id, exclude={}):
        database = DB.get_database()
        elements = database[collection].find_one(elem_id, exclude)
        return(elements)

    @staticmethod
    def get_keys_coll(collection, filter_={}, exclude={}):
        database = DB.get_database()
        keys = database[collection].find_one(filter_, exclude).keys()
        return(keys)

    @staticmethod
    def get_collections():
        database = DB.get_database()
        return(database.list_collection_names())

    @staticmethod
    def get_total_statistic():
        database = DB.get_database()
        cols_count = {}
        collections = DB.get_collections()
        for col in collections:
            cols_count[col] = database[col].find().count()
        return(cols_count)

    @staticmethod
    def update_one_elem(collection, id_, element_data):
        '''
        Updates one element and returns the number of updated elements
        '''
        database = DB.get_database()
        result = database[collection].update_one({'_id': id_}, {'$set': element_data})
        return(result.matched_count)

    @staticmethod
    def delete_elem(collection, id_):
        '''
        It does NOT delete, just update the field "Visible" to Fals
        '''
        result = DB.update_one_elem(collection, id_, {'visible': False})
        return(result)
