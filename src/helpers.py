from playhouse.shortcuts import model_to_dict
from playhouse.postgres_ext import fn

from peewee import Model, ModelSelect

import json

def vectorize(payload: dict):
    return fn.to_tsvector("english", " ".join([str(v) for v in payload.values()]))


def jsonify(collection: ModelSelect | Model, model: Model):
    if not collection: return json.dumps([])

    exclude_field_names = ["search_vector"]
    exclude = [getattr(model, field) for field in exclude_field_names]

    if hasattr(collection, '__iter__') and not isinstance(collection, dict):
        return json.dumps([model_to_dict(item, exclude=exclude) for item in collection], default=str)
    
    return json.dumps(model_to_dict(collection, exclude=exclude), default=str)