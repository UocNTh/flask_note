from flask import Flask , jsonify
from flask_restful import Resource, Api , reqparse 


app = Flask(__name__) 
app.config['BUNDLE_ERRORS'] = True
api = Api(app) 

class User(Resource) : 
    def post(self) : 

        parser = reqparse.RequestParser(bundle_errors=True) 
        parser.add_argument("name", type = str, help = "Name cannot be blank.",required = True) 
        parser.add_argument("email", type = str, help = "Email cannot be blank.", required = True) 
        args = parser.parse_args()

        return jsonify({"name" : args["name"] , "email" : args["email"]})

api.add_resource(User, '/user') 

if __name__ == "__main__" : 
    app.run(debug = True) 