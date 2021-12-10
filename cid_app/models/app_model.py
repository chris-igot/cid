import secrets
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
        self.admin_id = data["admin_id"] if "admin_id" in data else None
    @classmethod
    def find_admin_id(cls,admin_id):
        return cls.__find_cols__({"admin_id":admin_id})
    @classmethod
    def save(cls,form_data):
        form_data["id"] = secrets.token_urlsafe(16)
        form_data["key"] = secrets.token_urlsafe(16)
        return cls.__upsert__(form_data)