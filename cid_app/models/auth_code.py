import secrets
from cid_app.config.mysqlconnection import connectToMySQL
from cid_app.models.model_base import ModelBase
DB = "cid_db"

class AuthCode(ModelBase):
    table_name = "auth_codes"
    def __init__(self, data):
        ModelBase.__init__(self,data)
        print("AUTH CODE DATA",data)
        self.code = data["code"] if "code" in data else None
        self.app_id = data["app_id"] if "app_id" in data else None
        self.user_id = data["user_id"] if "user_id" in data else None
        self.status = data["status"] if "status" in data else None
        self.website_ = None
        self.user_ = None
    @classmethod
    def find_code(cls,code,app_id):
        data = {
            "code":code,
            "app_id":app_id
        }
        results = cls.__find_cols__(data)
        return results[0] if len(results) > 0 else None
    @classmethod
    def generate_code(cls,user_id,app_id):
        data = {
            "code": secrets.token_urlsafe(16),
            "app_id": app_id,
            "user_id": user_id,
            "status": "new"
        }
        cls.save(data)
        return data["code"]
    @classmethod
    def generate_code(cls,user_id,app_id):
        data = {
            "code": secrets.token_urlsafe(16),
            "app_id": app_id,
            "user_id": user_id,
            "status": "new"
        }
        cls.save(data)
        return data["code"]
    @classmethod
    def save(cls,data):
        # print("auth CLASS", list(cls({}).__dict__.keys()))
        instance_attrs = [attr for attr in list(cls({}).__dict__.keys()) if not attr.endswith("_")]
        attr_list = [attr for attr in data.keys() if data[attr] != None and attr in instance_attrs]

        if("user_id" in data and "app_id" in data and cls.__find_cols__({"user_id":data["user_id"],"app_id":data["app_id"]})):
            col_val_str = ",".join([f"`{col}`=%({col})s" for col in attr_list if col != "user_id" and col != "app_id"])

            query = f"UPDATE {cls.table_name} SET {col_val_str} WHERE user_id = %(user_id)s and app_id = %(app_id)s;"
            return connectToMySQL(cls.db_name).query_db(query,data)
        else:
            col_str = "`,`".join(attr_list)
            val_str = ",".join([f"%({col})s" for col in attr_list])

            query = f"INSERT INTO {cls.table_name} (`{col_str}`) VALUES ({val_str});"

            # print('insert',query,data)
            return connectToMySQL(cls.db_name).query_db(query,data)