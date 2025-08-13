from flask import Flask, render_template, request, jsonify
from game.rooms import rooms
from game.player import Player

app = Flask(__name__)
player = Player()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/game")
def index():
    return render_template("index.html")

@app.route("/comando", methods=["POST"])
def comando():
    cmd = request.json.get("cmd", "").lower().strip()
    message = ""

    if cmd.startswith("ir ") or cmd in ["norte","sul","leste","oeste","north","south","east","west"]:
        message = player.move(cmd, rooms)
    elif cmd in ["pegar"]:
        message = player.pick_item(rooms)
    elif cmd in ["olhar", "procurar", "look"]:
        message = "Você olha ao redor."
    else:
        message = "Comando não reconhecido."

    room_desc = player.look(rooms)

    return jsonify({
        "room_name": player.room,
        "room_desc": room_desc,
        "inventory": player.inventory,
        "message": message
    })

if __name__ == "__main__":
    app.run(debug=False)
