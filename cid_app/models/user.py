from cid_app.config.mysqlconnection import connectToMySQL
DB = "cid_db"

class User():
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
    @classmethod
    def find_id(cls,id):
        data = {
            "id":id
        }
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        if(results):
            results[0].pop('password',None)
            return results[0]
        else:
            return None
    @classmethod
    def find_email(cls,form_data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query,form_data)
        return results[0] if len(results) > 0 else None
    
    @classmethod
    def save(cls,form_data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(DB).query_db(query,form_data)