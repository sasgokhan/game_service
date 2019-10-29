import markdown
import os
import json

#import Framework
from flask import Flask
from flask_restful import Resource, Api

#import game_parser module to parse the website for each request
from game_parser import game_parser

# Create an Flask instance
app = Flask(__name__)

#Create the API for Flask instance
api = Api(app)

#Api will show the readme file when "/" requested
@app.route("/")

def index():
    """Present the documenttation of the API"""
    # Show the readme file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        # read the content of the file
        content = markdown_file.read()
        # convert it to html
        return markdown.markdown(content)


class GameList(Resource):
    def get(self):
        game_parser.store_games_info()
        with open(os.path.dirname(app.root_path) + '/data.txt', 'r') as json_file:
            games = json.load(json_file)
        return {'message': 'Success', 'data': games}, 200


class Game(Resource):
    def get(self, title):
        game_parser.store_games_info()
        with open(os.path.dirname(app.root_path) + '/data.txt', 'r') as json_file:
            games = json.load(json_file)
        for game in games['game']:
            if title == game['title']:
                return {'message': 'Game found', 'data': game}, 200

        # If the key does not exist in the data store, return a 404 error.
        return {'message': 'Game not found', 'data': {}}, 404


api.add_resource(GameList, '/games')
api.add_resource(Game, '/games/<string:title>')
