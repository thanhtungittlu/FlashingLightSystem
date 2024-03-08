import uuid
import datetime
import json
from pymongo import MongoClient
from configs import MongoConfig
from bson import ObjectId
from pymongo import WriteConcern

cf_db_name = MongoConfig.db_name

base_client = MongoClient(MongoConfig.uri)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif type(o) == datetime.date:
            a = datetime.datetime.combine(o, datetime.datetime.min.time())
            return a.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        elif type(o) == datetime.datetime:
            return o.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        elif isinstance(o, uuid.UUID):
            return str(o)
        elif isinstance(o, (bytes, bytearray)):
            return str(o, "utf-8")
        return json.JSONEncoder.default(self, o)


class BaseModel:
    client = base_client
    db_name = cf_db_name
    collection_name = ''

    def get_db(self):
        return self.client[self.db_name]

    def collector(self):
        return self.get_db()[self.collection_name]

    def insert(self, dictionary):
        return self.collector().insert_one(dictionary).inserted_id

    def insert_with_time(self, dictionary):
        dictionary['created_time'] = datetime.datetime.utcnow()
        dictionary['updated_time'] = datetime.datetime.utcnow()
        return self.insert(dictionary)

    def insert_many(self, dictionary):
        return self.collector().insert_many(dictionary).inserted_ids

    def insert_many_with_time(self, dictionary):
        for dic in dictionary:
            dic['created_time'] = datetime.datetime.utcnow()
            dic['updated_time'] = datetime.datetime.utcnow()
        return self.insert_many(dictionary)

    def write_concern(self, dictionary):
        collection = self.collector().with_options(
            write_concern=WriteConcern(w=0))
        collection.insert(dictionary)

    def update_one(self, id, dictionary):
        return self.collector().update_one(
            {"_id": ObjectId(id)},
            {
                "$set": dictionary
            }
        )

    def update_one_with_time(self, id, dictionary):
        dictionary['updated_time'] = datetime.datetime.utcnow()
        return self.update_one(id, dictionary)

    def upsert(self, search_option, dictionary):
        _now = datetime.datetime.utcnow()
        self.collector().update_one(
            filter=search_option,
            update={
                '$set': dictionary,
                "$setOnInsert": {'created_time': _now}
            },
            upsert=True
        )

    def upsert_with_time(self, search_option, dictionary):
        dictionary['updated_time'] = datetime.datetime.utcnow()
        return self.upsert(search_option, dictionary)

    def find_one(self, search_option, fields=None):
        if fields is not None:
            fields_show = {"_id": 0}
            for field in fields:
                fields_show[field] = 1
        else:
            fields_show = None

        return self.collector().find_one(search_option, fields_show)

    def count(self, search_option=None):
        if not search_option:
            search_option = {}
        return self.collector().find(search_option).count()

    def select_all(self, search_option, field_select=None):
        res = self.collector().find(search_option, field_select)
        return list(res)

    def delete_one(self, search_option):
        return self.collector().delete_one(search_option)

    def delete_many(self, search_option):
        return self.collector().delete_many(search_option)

    @staticmethod
    def normalize_uuid(some_uuid):
        if isinstance(some_uuid, str):
            return uuid.UUID(some_uuid)
        return some_uuid

    @staticmethod
    def normalize_object_id(some_object_id):
        if isinstance(some_object_id, str):
            return ObjectId(some_object_id)
        return some_object_id

    def update_one_query(self, query, data):
        return self.collector().update_one(
            query,
            {"$set": data}
        ).matched_count

    def update_one_query_with_time(self, query, data):
        data['updated_time'] = datetime.datetime.utcnow()
        return self.update_one_query(query, data)

    def update_many(self, query, data):
        return self.collector().update_many(
            query,
            {"$set": data}
        )

    def update_many_with_time(self, query, data):
        data['updated_time'] = datetime.datetime.utcnow()
        return self.update_many(query, data)
