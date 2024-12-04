from flask import Blueprint, request, jsonify
#from app import db
#from .models import User
from .openai_service import OpenAIService

api_blueprint = Blueprint('api', __name__)
chatGpt = OpenAIService()

@api_blueprint.route('/')
def home():
    return 'Hello, World!'

@api_blueprint.route('/users', methods=['POST'])
def add_user():
    username = request.json['username']
    email = request.json['email']
    
    #new_user = User(username=username, email=email)
    
    #db.session.add(new_user)
    #db.session.commit()
    
    #user_schema = UserSchema()
    #return user_schema.jsonify(new_user), 201
    return jsonify({"result": "ok"}), 200

@api_blueprint.route('/users', methods=['GET'])
def get_users():
    #users = User.query.all()
    #user_schema = UserSchema(many=True)
    #return user_schema.jsonify(users)
    return jsonify({"result": "ok"}), 200

@api_blueprint.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    #user = User.query.get_or_404(id)
    #user_schema = UserSchema()
    #return user_schema.jsonify(user)
    return jsonify({"result": "ok"}), 200

@api_blueprint.route('/prompt', methods=['POST'])
def openai_get():
    data = request.get_json()
    prompt = data.get("content")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    response = chatGpt.get_response(prompt)

    return response.choices[0].message.content