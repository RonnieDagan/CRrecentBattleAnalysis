from flask import Flask, render_template, request, jsonify, redirect, url_for
from battle_fetch import recBattles
from sample_output import sample_output

api_key = ''

app = Flask(__name__)

def remove_first_instance(string, char):
    index = string.find(char)
    if index != -1:
        return string[:index] + string[index + 1:]
    return string

def get_battle_info(player_tag):
    global recent_battles
    # rb = recBattles(api_key, player_tag)
    recent_battles = sample_output
    
    battles_info = []
    
    for battle in recent_battles:
        player = battle["team"]["name"]
        player_tag = remove_first_instance(battle["team"]["tag"], '#')
        opponent = battle["opponent"]["name"]
        opponent_tag = remove_first_instance(battle["opponent"]["tag"], '#')
        winner = player if battle["team"]["win_status"] == "win" else opponent
        player_crowns = battle["team"]["crowns"]
        player_trophies = battle["team"]["startingTrophies"]
        opponent_trophies = battle["opponent"]["startingTrophies"]
        opponent_crowns = battle["opponent"]["crowns"]
        
        player_deck = []
        opponent_deck = []
        for card in battle["team"]["deck"]:
            if "iconUrl" in card:
                player_deck.append(card["iconUrl"])
        for card in battle["opponent"]["deck"]:
            if "iconUrl" in card:
                opponent_deck.append(card["iconUrl"])
        
        battle_info = {
            "player": player,
            "player_tag": player_tag,
            "opponent": opponent,
            "opponent_tag": opponent_tag,
            "winner": winner,
            "player_crowns": player_crowns,
            "player_trophies": player_trophies,
            "opponent_trophies": opponent_trophies,
            "opponent_crowns": opponent_crowns,
            "player_deck": player_deck,
            "player_deck1": player_deck[0:4],
            "player_deck2": player_deck[4:9],
            "opponent_deck": opponent_deck,
            "opponent_deck1": opponent_deck[0:4],
            "opponent_deck2": opponent_deck[4:9],
        }
        
        battles_info.append(battle_info)
    
    return battles_info

@app.route('/analyze', methods=['GET'])
def analyze():
    # Perform analysis here
    
    analysis_result = ""
    return jsonify({'analysis_result': analysis_result})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    player_tag = request.form['player_tag']
    return redirect(url_for('show_battles', player_tag=player_tag))

@app.route('/<player_tag>', methods=['GET'])
def show_battles(player_tag):
    battles_info = get_battle_info(player_tag)
    return render_template('battles.html', battles=battles_info)

if __name__ == '__main__':
    app.run(debug=True, port=3000)