from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #classmethod to read data from the user table
    @classmethod
    def get_all(cls):
        #set up our sql statement, in this case a SELECT
        query = "SELECT * FROM users;"
        #sending the query to the database and storing the result in results
        results = connectToMySQL('users_schema').query_db(query)
        #declaring a new list for each user to be held
        users = []
        #iterates through the results and places each user's selected information into a dictionary which then get stored in the users list
        for user in results:
            users.append(cls(user))
        return users

    #method to return the data from a single user
    @classmethod
    def get_user(cls,data):
        query = "SELECT * FROM users WHERE id =%(id)s;"
        results = connectToMySQL('users_schema').query_db(query,data)
        print(results)
        return results

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users(first_name,last_name,email,created_at,updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() );"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def edit_user(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)