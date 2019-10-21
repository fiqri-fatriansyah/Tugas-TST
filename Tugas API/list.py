from flask import make_response, abort

BOARD_GAME = {
    "0": {
        "id": "0",
        "name": "Talisman",
        "publisher": "Asmodus Inc.",
        "quantity" : 1
    },
    "1": {
        "id": "1",
        "name": "Portal",
        "publisher": "Valve Inc.",
        "quantity" : 5
    },
    "2": {
        "id": "2",
        "name": "Portal 2",
        "publisher": "Valve Inc.",
        "quantity" : 2
    }
}

def read():
    # Create the list of board game from our data
    return [BOARD_GAME[key] for key in sorted(BOARD_GAME.keys())]

def read_one(id):
    # Create a single board game from our data
    if id in BOARD_GAME:
        boardgame_temp = BOARD_GAME.get(id)
    else:
        abort(
            404, "Board game with id {id} not found".format(id=id)
        )
    return boardgame_temp

def create(boardgame):
    id = boardgame.get("id", None)
    name = boardgame.get("name", None)
    publisher = boardgame.get("name", None)
    quantity = str(boardgame.get("quantity", None))

    #Is exist?
    if boardgame not in BOARD_GAME and id is not None:
        BOARD_GAME[id] = {
            "id" : id,
            "name" : name,
            "publisher" : publisher,
            "quantity" : quantity
        }
        return make_response(
            "Board game {name} has been created successfully!".format(name = name), 201
        )
    else:
        abort(
            406, "Board game already exist."
        )
