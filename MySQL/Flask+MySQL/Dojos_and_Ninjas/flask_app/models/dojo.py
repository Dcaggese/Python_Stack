from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    #get_all class to pull all data from the dojos table
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def add_dojo(cls,data):
        query = "INSERT INTO dojos(name,created_at,updated_at) VALUE(%(name)s,NOW(),NOW());"
        return connectToMySQL('dojo_and_ninjas_schema').query_db(query,data)

    @classmethod
    def get_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojo_and_ninjas_schema').query_db(query,data)
        return result

    @classmethod
    def get_dojo_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query,data)

        ninjas = []
        for dict in results:
            ninja = cls(dict)

            ninja_data = {
                'id' : dict['ninjas.id'],
                'first_name' : dict['first_name'],
                'last_name' : dict['last_name'],
                'age' : dict['age'],
                'created_at' : dict['ninjas.created_at'],
                'updated_at' : dict['ninjas.updated_at'],
                'dojo_id' : dict['dojo_id']
            }

            creator = Ninja(ninja_data)
            ninja.creator = creator
            ninjas.append(ninja)
        print(ninjas[0])
        return ninjas

