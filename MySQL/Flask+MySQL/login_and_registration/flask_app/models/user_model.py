import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validate_user(data):
        is_valid = True
        found_user =  User.get_email(data)
        if len(data['first_name']) < 3:
            flash("First name must be at least 3 Characters")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("Last name must be at least 3 Characters")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email format")
            is_valid = False
        if found_user:
            flash("Account already exists")
            is_valid = False
        if len(data['password']) < 7:
            flash("Password must be at least 8 Characters")
            is_valid = False
        if data['password'] != data['password_verification']:
            flash("Passwords do not match")
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True

        found_user =  User.get_email(data)

        if found_user:
            if not bcrypt.check_password_hash(found_user.password, data['password']):
                is_valid = False
            
            pass
        else:
            is_valid = False
            
        if not is_valid:
            flash('Invalid login.')

        return is_valid

    @classmethod
    def create_user(cls,data):
        query = """
        INSERT INTO users(first_name,last_name,email,password,created_at,updated_at) 
        VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW());
        """
        return connectToMySQL('login_and_registration').query_db(query,data)

    @classmethod
    def get_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('login_and_registration').query_db(query,data)

        if not results or len(results) < 1:
            return False
        else:
            return cls(results[0])