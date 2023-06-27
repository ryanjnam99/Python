from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import magazines
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    DB = "magazine_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.magazines = []

    @classmethod
    def save(cls, data):
        query = """INSERT into users (first_name, last_name, email, password) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
        return connectToMySQL("magazine_schema").query_db(query,data)

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("magazine_schema").query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("magazine_schema").query_db(query,data)
        # Didn't find a matching user
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def edit_user(cls, data):
        query="""UPDATE users SET first_name = %(first_name)s,
            last_name = %(last_name)s, email= %(email)s
            WHERE id = %(id)s;"""
        return connectToMySQL("magazine_schema").query_db(query,data)

    
    @classmethod 
    def get_user_with_magazines(cls,data):
        query = """SELECT * FROM users LEFT JOIN 
        magazines ON magazines.user_id = users.id
        WHERE users.id = %(id)s;"""
        results = connectToMySQL("magazine_schema").query_db(query,data)
        print(results)
        one_user = cls(results[0])
        for user_row in results:
            magazine_data = {
                "id": user_row['magazines.id'],
                "description": user_row['description'],
                "name": user_row['name'],
                "created_at": user_row['magazines.created_at'],
                "updated_at": user_row['magazines.updated_at'],
                "user_id": user_row['user_id']
            }
            one_user.magazines.append(magazines.Magazine(magazine_data))
        return one_user

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Password does not match")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_email(user):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("magazine_schema").query_db(query,user)
        print(results)
        is_valid = True
        if len(results) >= 1:
            flash("Email already entered!")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_update(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid





