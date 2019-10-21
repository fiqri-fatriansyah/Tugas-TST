BOARD_GAME = {
    "Talisman": {
        "id": 1,
        "name": "Talisman",
        "publisher": "Asmodus Inc.",
        "quantity" : 1
    },
    "Portal": {
        "id": 2,
        "name": "Portal",
        "publisher": "Valve Inc.",
        "quantity" : 5
    },
    "Portal 2": {
        "id": 3,
        "name": "Portal 2",
        "publisher": "Valve Inc.",
        "quantity" : 2
    }
}

def read():
    # Create the list of people from our data
    return [BOARD_GAME[key] for key in sorted(BOARD_GAME.keys())]
