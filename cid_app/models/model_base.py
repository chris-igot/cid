from cid_app.config.mysqlconnection import connectToMySQL
DB = "cid_db"

class ModelBase():
    table_name = "base_tname_clvar"
    db_name = DB
    def __init__(self, data):
        self.id = data["id"] if "id" in data else None
    @classmethod
    def __find_id__(cls,id):
        query = f"SELECT * FROM {cls.table_name} WHERE id = %(id)s;"
        result = connectToMySQL(cls.db_name).query_db(query,{"id":id})
        # print(query,result)
        return cls(result[0]) if len(result)>0 else None
    @classmethod
    def __find_cols__(cls, data):
        model_attr_list = list(cls({}).__dict__.keys())
        valid_cols = [col for col,val in data.items() if val != None and col in model_attr_list]
        # print(valid_cols)
        col_val_str = " and ".join([f"`{col}`=%({col})s" for col in valid_cols])
        query = f"SELECT * FROM {cls.table_name} WHERE {col_val_str};"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print("\n\nRESULTS",results,query)
        output = []
        if(results):
            output = [cls(result) for result in results]
        print(query,output,"\n\n")
        return output
    @classmethod
    def __upsert__(cls,data):
        # print("TEST CLASS", cls.table_name)
        instance_attrs = [attr for attr in list(cls({}).__dict__.keys()) if not attr.endswith("_")]
        attr_list = [attr for attr in data.keys() if data[attr] != None and attr in instance_attrs]

        if("id" in data and cls.__find_id__(data["id"])):
            col_val_str = ",".join([f"`{col}`=%({col})s" for col in attr_list if col != "id"])

            query = f"UPDATE {cls.table_name} SET {col_val_str} WHERE id = %(id)s;"

            # print('update',query)
            connectToMySQL(cls.db_name).query_db(query,data)
            return cls.id
        else:
            col_str = ",".join(attr_list)
            val_str = ",".join([f"%({col})s" for col in attr_list])

            query = f"INSERT INTO {cls.table_name} ({col_str}) VALUES ({val_str});"

            # print('insert',query)
            return connectToMySQL(cls.db_name).query_db(query,data)
