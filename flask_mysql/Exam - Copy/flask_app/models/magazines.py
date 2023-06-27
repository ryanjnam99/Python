from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import users

class Magazine:
    DB = "magazine_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save_magazine(cls,data):
        query="""INSERT INTO magazines (name, description, user_id) 
        VALUES (%(name)s, %(description)s, %(user_id)s);"""
        return connectToMySQL("magazine_schema").query_db(query,data)

    @classmethod
    def get_all_magazines(cls):
        query = """SELECT * FROM magazines JOIN users ON
        magazines.user_id = users.id"""
        results = connectToMySQL('magazine_schema').query_db(query)
        magazines = []
        for row in results:
            one_magazine = cls(row)
            user_data = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email" : row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            one_magazine.author = users.User(user_data)
            magazines.append(one_magazine)
        return magazines
    
    @classmethod
    def get_magazine(cls,data):
        query="SELECT * FROM magazines WHERE id = %(id)s;"
        results = connectToMySQL("magazine_schema").query_db(query,data)
        return cls(results[0])

    @classmethod
    def delete_magazine(cls,data):
        query = "DELETE from magazines where id = %(id)s;"
        return connectToMySQL('magazine_schema').query_db(query,data)

    @staticmethod
    def validate_magazine(user):
        is_valid = True
        if len(user['name']) < 2:
            flash("Title must at least be 2 characters long")
            is_valid = False
        if len(user['description']) < 10:
            flash("Description must at least 10 characters long.")
            is_valid = False
        return is_valid
