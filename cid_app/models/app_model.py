from cid_app.config.mysqlconnection import connectToMySQL
from cid_app.models.model_base import ModelBase
DB = "cid_db"

class AppModel(ModelBase):
    table_name = "apps"
    def __init__(self, data):
        ModelBase.__init__(self,data)
        self.name = data["name"] if "name" in data else None
        self.callback = data["callback"] if "callback" in data else None
        self.key = data["key"] if "key" in data else None
