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
        result = connectToMySQL(DB).query_db(query,data)[0]
        result.pop('password',None)
        return result
    @classmethod
    def find_email(cls,form_data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DB).query_db(query,form_data)[0]
        return result
    
    @classmethod
    def save(cls,form_data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(DB).query_db(query,form_data)