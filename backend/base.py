from flask import Flask, request
from flask_cors import CORS, cross_origin

api = Flask(__name__)
CORS(api, support_credentials=True)

@api.route('/profile')
@cross_origin()
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body