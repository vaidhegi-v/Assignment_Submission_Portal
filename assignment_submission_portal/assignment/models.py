# models.py
import datetime
import bcrypt
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['assignment_portal_db']

class User:
    @staticmethod
    def create_user(data):
        user = db.users.find_one({'username': data['username']})
        if user:
            return {'error': 'User already exists'}
        data['password'] = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        db.users.insert_one(data)
        return {'message': 'User registered successfully'}

    @staticmethod
    def login(data):
        user = db.users.find_one({'username': data['username']})
        if user and bcrypt.checkpw(data['password'].encode('utf-8'), user['password']):
            # Generate token (use python-jwt or other methods)
            return {'message': 'Login successful', 'token': 'sample-token'}
        return {'error': 'Invalid credentials'}

class Assignment:
    @staticmethod
    def create_assignment(data):
        assignment = {
            'userId': data['userId'],
            'task': data['task'],
            'admin': data['admin'],
            'timestamp': datetime.datetime.now(),
            'status': 'pending'
        }
        db.assignments.insert_one(assignment)
        return {'message': 'Assignment uploaded'}

    @staticmethod
    def get_admin_assignments(admin):
        return list(db.assignments.find({'admin': admin}))

    @staticmethod
    def update_assignment_status(assignment_id, status):
        db.assignments.update_one(
            {'_id': assignment_id}, 
            {'$set': {'status': status}}
        )
        return {'message': f'Assignment {status}'}
