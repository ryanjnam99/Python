from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    DB = "dojo_survey_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # @classmethod
    # def save (cls,data):
    #     query = "INSERT INTO surveys (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
    #     return connectToMySQL("dojo_survey_schema").query_db(query,data)
    
    @staticmethod
    def validate_survey(surveys):
        is_valid = True
        if len(surveys['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(surveys['location']) == 0:
            flash("Must type in location.")
            is_valid = False
        if len(surveys['language']) == 0:
            flash("Must select language.")
            is_valid = False
        if len(surveys['comment']) == 0:
            flash("Must type in at least 3 characters.")
            is_valid = False
        return is_valid
