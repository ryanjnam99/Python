from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas

class Dojo:
    DB = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def save (cls, data):
        query="INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
    
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        print(results)
        one_dojo = cls(results[0])
        for ninja_row in results:
            ninja_data = {
                "id": ninja_row["ninjas.id"],
                "first_name": ninja_row["first_name"],
                "last_name" : ninja_row["last_name"],
                "age" : ninja_row["age"],
                "dojo_id":  ninja_row["dojo_id"]
            }
            one_dojo.ninjas.append(ninjas.Ninja(ninja_data))
        return one_dojo


