from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) <= 3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if len(dojo['location']) <= 3:
            flash("Location must be at least 3 characters")
            is_valid = False
        if dojo['language'] != 'Python':
            flash("Select your favorite language")
            is_valid = False
        return is_valid

    @classmethod
    def add_dojos(cls,data):
        query = "INSERT INTO dojos(name,location,langauge,comment,created_at,updated_at) VALUES(%(id)s,%(name)s,%(location)s,%(language)s,%(comment)s,NOW(),NOW());"
        return connectToMySQL('dojo_survey_schema').query_db(query,data)

