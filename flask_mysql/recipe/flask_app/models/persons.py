from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import recipes
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Person:
    DB = "recipe_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    @classmethod
    def save(cls, data):
        query = """INSERT INTO persons (first_name, last_name, email, password) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
        return connectToMySQL("recipe_schema").query_db(query,data)

    @classmethod
    def get_person(cls, data):
        query = "SELECT * FROM persons WHERE id = %(id)s;"
        results = connectToMySQL("recipe_schema").query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM persons WHERE email = %(email)s;"
        results = connectToMySQL("recipe_schema").query_db(query,data)
        # Didn't find a matching user
        if len(results) < 1:
            return False
        return cls(results[0])

    # @classmethod
    # def get_user_with_recipes(cls, data):
    #     query = """SELECT * FROM persons LEFT JOIN 
    #     recipes ON recipes.person_id = persons.id
    #     WHERE persons.id = %(id)s"""
    #     results = connectToMySQL("recipe_schema").query_db(query,data)
    #     print(results)
    #     one_user = cls(results[0])
    #     for recipe_row in results:
    #         recipe_data = {
    #             "id": recipe_row['recipes.id'],
    #             "name": recipe_row['name'],
    #             "description": recipe_row['description'],
    #             "time": recipe_row['time'],
    #             "instructions": recipe_row['instructions'],
    #             "created_at": recipe_row['created_at'],
    #             "updated_at": recipe_row['updated_at'],
    #             "person_id": recipe_row['person_id']
    #         }
    #         one_user.recipes.append(recipes.Recipe(recipe_data))
    #     return one_user
        
    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Password does not match")
            is_valid = False
        # if user['passowrd'] == '':
        #     flash("The password is empty!")
        #     is_valid = False
        return is_valid

    @staticmethod
    def validate_email(user):
        query = "SELECT * FROM persons WHERE email = %(email)s;"
        results = connectToMySQL("recipe_schema").query_db(query,user)
        print(results)
        is_valid = True
        if len(results) >= 1:
            flash("Email already entered!")
            is_valid = False
        return is_valid





