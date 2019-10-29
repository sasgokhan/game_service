import pytest
import requests
from game_registry import Game, GameList

# Test for readme file is accessible from index
def test_readme():

    url='http://localhost:5000'
    req = requests.get(url)
    assert req.status_code == 200

# Test for getting the game list
def test_get_gamelist():

    gamelist = GameList()
    url = "http://localhost:5000/games"
    resp_url = requests.get(url)
    resp = gamelist.get()
    assert resp[1] == 200
    assert resp_url.status_code == 200, resp.text

# Test for a successful get request
def test_get_successfull_gameinfo():

    game = Game()
    title = "Monster Hunter: World - Iceborne"
    url = "http://localhost:5000/games/" + title
    resp_url = requests.get(url)
    resp = game.get(title)
    assert resp[1] == 200
    assert resp_url.status_code == 200, resp.text

# Test for a unsuccessful get request
def test_get_notavailable_game():
    game = Game()
    title = 'No game like this'
    resp = game.get(title)
    assert resp[1] == 404


if __name__ == '__main__':
    pytest.main()



