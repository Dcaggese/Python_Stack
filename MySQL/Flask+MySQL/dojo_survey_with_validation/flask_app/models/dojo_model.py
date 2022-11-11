from flask_app.config.mysqlconnection import connectToMySQL

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
        pass

    @classmethod
    def add_dojos(cls,data):
        query = "INSERT INTO dojos(name,location,langauge,comment,created_at,updated_at) VALUES(%(id)s,%(name)s,%(location)s,%(language)s,%(comment)s,NOW(),NOW());"
        return connectToMySQL('dojo_survey_schema').query_db(query,data)

