from flask import Flask, render_template, request
from battle_fetch import recBattles
from analysis import analyze_battles

api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijk2MDVlMGM0LTU1NWMtNGZkNS1iZTU2LTBlZTc4YjBmMjc1YyIsImlhdCI6MTcxNDk2OTUwOSwic3ViIjoiZGV2ZWxvcGVyLzc0NTYzNDA3LWZhMTQtMmQyNS0xYTIzLTMwM2Y5YWI1NTQxYyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzIuODguNzIuMTA4Il0sInR5cGUiOiJjbGllbnQifV19.QPzzbfp09HCdLTZgOzwhpoj5SRRl4r-fy2EF044pZGvCpblWoBVEKe-GWXtygo1zk1ryq0jadXxB9kmaMfETSw'

app = Flask(__name__)

def get_battle_info(player_tag):
    global recent_battles
    rb = recBattles(api_key, player_tag)
    recent_battles = rb.recent_battles()
    
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

@app.route('/', methods=['GET'])
def index():
    

    return render_template('index.html')


@app.route('/', methods=['POST'])
def submit():
    player_tag = request.form['player_tag']
    battles_info = get_battle_info(player_tag)
    analysis_result = analyze_battles(recent_battles)
    return render_template('battles.html', battles=battles_info, analysis_result=analysis_result)

if __name__ == '__main__':
    app.run(debug=True)