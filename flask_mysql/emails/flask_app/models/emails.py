from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Email:
    DB = "email_schema"
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL("email_schema").query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL("email_schema").query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails
    
    @staticmethod
    def validate_email(user):
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL("email_schema").query_db(query,user)
        print(results)
        is_valid = True
        if len(results) >= 1:
            flash("Email already entered!")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid
