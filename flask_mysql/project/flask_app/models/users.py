from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    DB = "crave_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """INSERT into users (name, email, password) 
        VALUES (%(name)s, %(email)s, %(password)s);"""
        return connectToMySQL("crave_schema").query_db(query,data)

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("crave_schema").query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("crave_schema").query_db(query,data)
        # Didn't find a matching user
        if len(results) < 1:
            return False
        return cls(results[0])

    
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['name']) < 2:
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
        results = connectToMySQL("crave_schema").query_db(query,user)
        print(results)
        is_valid = True
        if len(results) >= 1:
            flash("Email already entered!")
            is_valid = False
        return is_valid





