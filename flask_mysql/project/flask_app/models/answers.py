from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import users

class Answer:
    DB = "crave_schema"
    def __init__(self, data):
        self.id = data['id']
        self.scale = data['scale']
        self.crave = data['crave']
        self.price = data['price']
        self.cuisine = data['cuisine']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.past_request = []
        
    @classmethod
    def save_answer(cls,data):
        query = """INSERT INTO answers (scale, crave, price, cuisine)
        VALUES (%(scale)s, %(crave)s, %(price)s, %(cuisine)s);"""
        return connectToMySQL("crave_schema").query_db(query,data)
