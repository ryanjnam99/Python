from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import persons

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
        query = """SELECT * FROM recipes 
        JOIN persons ON recipes.person_id = persons.id;"""
        results = connectToMySQL('recipe_schema').query_db(query)
        recipes = []
        for one_row in results:
            one_recipe = cls(one_row)
            person_data = {
                "id": one_row['persons.id'],
                "first_name": one_row["first_name"],
                "last_name": one_row["last_name"],
                "email": one_row['email'],
                "password": one_row['password'],
                "created_at": one_row['persons.created_at'],
                "updated_at": one_row['persons.updated_at']
            }
            one_recipe.chef = persons.Person(person_data)
            recipes.append(one_recipe)
        return recipes

    @classmethod
    def save_recipe(cls, data):
        query = """INSERT INTO recipes (name, description, time, instructions, person_id)
        VALUES (%(name)s, %(description)s, %(time)s, %(instructions)s, %(person_id)s)"""
        return connectToMySQL("recipe_schema").query_db(query,data)

    @classmethod
    def get_recipe(cls, data):
        query = """SELECT * FROM recipes WHERE id = %(id)s;"""
        results = connectToMySQL("recipe_schema").query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def edit_recipe(cls, data):
        query = """UPDATE recipes SET name = %(name)s, 
            description = %(description)s,
            time = %(time)s, instructions = %(instructions)s 
            WHERE id = %(id)s;"""
        return connectToMySQL('recipe_schema').query_db(query,data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes where id = %(id)s"
        return connectToMySQL('recipe_schema').query_db(query,data)


    @staticmethod
    def validate_recipe(user):
        is_valid = True
        if len(user['description']) == 0:
            flash("Description must not be left blank")
            is_valid = False
        if len(user['name']) == 0:
            flash("Name must not be blank")
            is_valid = False
        if 'time' not in user:
            flash("Is it under 30 minutes?")
        if len(user['instructions']) == 0:
            flash("Instructions must not be blank")
            is_valid = False
        return is_valid

