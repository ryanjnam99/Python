from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe: 
    DB: "recipe_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description= data['description']
        self.time = data['time']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.person_id = data['person_id']
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipe_schema').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def save_recipe(cls, data):
        query = """INSERT INTO recipes (name, description, time, instructions, person_id)
        VALUES (%(name)s, %(description)s, %(time)s, %(instructions)s, %(person_id)s)"""
        return connectToMySQL("recipe_schema").query_db(query,data)
    
    @staticmethod
    def validate_recipe(user):
        is_valid = True
        if len(user['description']) == 0:
            flash("Description must not be left blank")
            is_valid = False
        if len(user['name']) == 0:
            flash("Name must not be blank")
            is_valid = False
        if len(user['instructions']) == 0:
            flash("Instructions must not be blank")
            is_valid = False
        return is_valid

