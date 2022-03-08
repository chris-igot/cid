from cid_app.config.mysqlconnection import connectToMySQL
from cid_app.models.model_base import ModelBase

class User(ModelBase):
    table_name = "users"
    def __init__(self, data):
        ModelBase.__init__(self,data)
        self.id = data["id"] if "id" in data else None
        self.first_name = data["first_name"] if "first_name" in data else None
        self.last_name = data["last_name"] if "last_name" in data else None
        self.email = data["email"] if "email" in data else None
        self.password = data["password"] if "password" in data else None
    @classmethod
    def find_id(cls,id):
        return cls.__find_id__(id)
    @classmethod
    def find_email(cls,form_data):
        data = {"email":form_data["email"]}

        return cls.__find_cols__(data)[0] if len(cls.__find_cols__(data)) > 0 else None
    @classmethod
    def save(cls,form_data):
        return cls.__upsert__(form_data)
        