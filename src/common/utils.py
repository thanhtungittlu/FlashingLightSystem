"""
This is the place where common functions are kept
"""
from bson import Int64
from decimal import Decimal
from bson.objectid import ObjectId
from enum import Enum
import uuid

def to_dict(obj, **kwargs):
    time_format = '%Y-%m-%dT%H:%M:%S.%sZ'
    if 'time_format' in kwargs:
        time_format = kwargs['time_format']

    if isinstance(obj, Int64):
        return int(obj)

    if _isnamedtupleinstance(obj):
        return to_dict(obj._asdict())

    if isinstance(obj, dict):
        data = {}
        for (key, value) in obj.items():
            data[key] = to_dict(value)
        return data

    if hasattr(obj, '_ast'):
        return to_dict(obj._ast())

    if hasattr(obj, '__iter__') and not isinstance(obj, str):
        return [to_dict(value) for value in obj]

    if hasattr(obj, '__dict__'):
        return dict(
            [
                (key, to_dict(_handling_specific_type(value, time_format) or value))
                for key, value in obj.__dict__.items()
                if not callable(value) and not key.startswith('_')
            ]
        )

    return _handling_specific_type(obj, time_format) or obj

def _isnamedtupleinstance(x):
    t = type(x)
    b = t.__bases__
    if len(b) != 1 or b[0] != tuple:
        return False
    f = getattr(t, '_fields', None)
    if not isinstance(f, tuple):
        return False
    return all(type(n) == str for n in f)


def _handling_specific_type(value, time_format):
    from datetime import datetime

    if isinstance(value, ObjectId):
        return str(value)

    if isinstance(value, Decimal):
        return float(value)

    if isinstance(value, datetime):
        if not value.microsecond:
            time_format = '%Y-%m-%dT%H:%M:%S.000000Z'
        else:
            time_format = '%Y-%m-%dT%H:%M:%S.%fZ'
        return datetime.strftime(value, time_format)

    # if isinstance(value, date):
    #     return value.isoformat()

    if isinstance(value, Enum):
        return value.value

def validate_uuid(uuid_str):
    try:
        uuid.UUID(uuid_str)
        return True
    except ValueError:
        return False
