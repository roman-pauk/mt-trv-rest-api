from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import autenticate, identity

app = Flask(__name__)
app.secret_key = 'mountain-travel-romans-key'
api = Api(app)
jwt = JWT(app, autenticate, identity)

travels = []

class Travel(Resource):
    # @jwt_required()
    def get(self, title):
        trv = next(filter(lambda t: t['title'] == title, travels), None)
        if trv:
            return trv
        return {'message': 'travel not found'}, 400

class Travels(Resource):
    def get(self):
        return travels

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help="Title cann't be empty")
        parser.add_argument('text', type=str, required=True, help="Text cann't be empty")

        data = parser.parse_args()
        trv = {
            'title': data['title'],
            'text': data['text'],
        }
        travels.append(trv)

        return trv

api.add_resource(Travel, '/travel/<string:title>')
api.add_resource(Travels, '/travels')

app.run(port=5000, debug=True)