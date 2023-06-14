from mysqlconnection import connectToMySQL

class User:
    DB = "users_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (name, last_name, email) VALUES (%(name)s, %(last_name)s, %(email)s);"
        return connectToMySQL('users_schema').query_db(query, data)