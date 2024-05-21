from flask import Flask, render_template, request, jsonify
from battle_fetch import recBattles
from sample_output import sample_output

api_key = ''

app = Flask(__name__)

def get_battle_info(player_tag):
    global recent_battles
    # rb = recBattles(api_key, player_tag)
    recent_battles = sample_output
    
    battles_info = []
    
    for battle in recent_battles:
        player = battle["team"]["name"]
        opponent = battle["opponent"]["name"]
        winner = player if battle["team"]["win_status"] == "win" else opponent
        player_crowns = battle["team"]["crowns"]
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
            "opponent": opponent,
            "winner": winner,
            "player_crowns": player_crowns,
            "opponent_crowns": opponent_crowns,
            "player_deck": player_deck,
            "opponent_deck": opponent_deck
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


@app.route('/', methods=['GET', 'POST'])
def submit():
    player_tag = request.form['player_tag']
    battles_info = get_battle_info(player_tag)
    return render_template('battles.html', battles=battles_info)



if __name__ == '__main__':
    app.run(debug=True, port=8000)