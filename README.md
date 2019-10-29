
# Game Information Service
    This Service provides information of Top PlayStation-4 games based on Metacritic’s PS4 page:

***    http://www.metacritic.com/game/playstation-4***

The Service does following:
    It parses game data from above webpage and generates a data store of the games which is consisting
        an array of JSON elements.

    It provides an API to get information about all games or a specific game if it is in the top game list.

    It provides information about usage of service and details about it

# Details

***    REST API Definition***

A HTTP “GET” request at “/games” returns all top PS4 games on metacritic page

A HTTP “GET” request at “/games/TITLE_OF_THE_GAME” returns information in  JSON for a specific game.

A HTTP "GET" request at "/" returns html converted Readme file of the service

###All responses will be as below:

´´´json

{

        "title": Title of the game

        "score": Score of the game

        "description": Description of the game
}

´´´

            Subsequent response definition will only detail the expected value of the "data field"

# List all games

***Request*** :
  ´GET /games´

**Response**
- ´200 OK´ on success

´´´json

[

        {

        "title": "Title of the game"

        "score": "Score of the game"

        "description": Description of the game

        },

        {

        "title": "Title of the game"

        "score": "Score of the game"

        "description": Description of the game

        }

]

´´´

#Lookup a specific game

***Request*** :

        GET /games/title of the game

**Response**

- ´404 not found´ if the game doesnt exist

- ´200 OK´ on success together with game data in json format as below:

´´´
    json

        {

            "title": "Title of the game"

            "score": "Score of the game"

            "description": Description of the game

        }

´´´

#Service usage Procedure

    The service has been written in python 3.

    The service is Dockerized a Dockerfile and Docker-Compose File has been used to automate the build and run.

    The requirements installation to use this service has been automated as well.

    To improve the flexibility and isolation of the tasks. The service consisting 2 different modules

***        game_parser module:*** Parses to information and regenerates the data store in every request

***        game_registry module:*** Provides a REST API to get information of  list of games or a specific game.

    To start service, go to main folder of the repository and just type below command:
***        docker-compose up***

#    Accessing Resources

        http://localhost:5000 to access Readme file

        http://localhost:5000/games : To access information of all top playstation-4 games

        http://localhost:5000/games/<title of the game> : to access information of a specific playstation-4 game

#      Running the tests

    pytest has been used for unittesting for below cases
        a successful game retrieval
        an unsuccessful game retrieval
        a succesful gamelist retrieval
        a successful readme file retrieval
        a succesful get request to the urls (for all cases)


*** how to run tests:***

    tests are defined at test_game_registry.py file at /game_registry folder
    the service should be started before running the tests.

    go to game_registry folder and run:
***     pytest  test_game_registry.py***

















