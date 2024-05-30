# Todo: make buttons load
# Style Strengths, Weaknesses, etc
# Leaderboard
from flask import Flask, render_template, request, jsonify, redirect, url_for
from battle_fetch import recBattles
from analysis import ai_analyze
from compare import ai_compare

weaknesses = ""
strengths = ""
summary = ""
ptag = ""

api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE2Y2E0NmY1LWVlMDctNDU4OC1iNDZhLTg5Nzg1YTJmMmFiZCIsImlhdCI6MTcxNzAzMzM1OSwic3ViIjoiZGV2ZWxvcGVyLzc0NTYzNDA3LWZhMTQtMmQyNS0xYTIzLTMwM2Y5YWI1NTQxYyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIyMC4xNjkuMjguMjEwIl0sInR5cGUiOiJjbGllbnQifV19.hODUgwFBPTo4qBjOrApPt8ctBEvqusqNig82aPeZ1aCVBd8VR9dbi4h6eqKTK7fzX0h2PDaxNhg1ehRfH7n3fw'

app = Flask(__name__)


def list_to_string(li):
    return ', '.join(map(str, li))

def format_ai(ai_text):
    temp = ai_text.split("\n")
    strengths = []
    weaknesses = []
    summary = ""
    mode = 0
    for i in range(len(temp)):
        temp2 = temp[i].split(" ")
        if temp2[0] == "Cards" or temp2[0] == "Summary:":
            mode+=1
        if mode == 1:
            if temp2[0] != "Cards" and temp2[0] != "Summary:" and temp2[0] != '':
                strengths.append(temp[i])
        if mode == 2: 
            if temp2[0] != "Cards" and temp2[0] != "Summary:" and temp2[0] != '':
                weaknesses.append(temp[i])
        if mode == 3:
            for word in temp2:
                if word != 'Summary:':
                    summary+= word + ' '
        summary.rstrip()
    return [strengths, weaknesses, summary]

def remove_first_instance(string, char):
    index = string.find(char)
    if index != -1:
        return string[:index] + string[index + 1:]
    return string

def get_battle_info(player_tag):
    global recent_battles
    rb = recBattles(api_key, player_tag)
    recent_battles = rb.recent_battles()
    
    battles_info = []
    
    for battle in recent_battles:
        mode = battle["game_info"]["mode"]
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
            "mode": mode,
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
            "player_deck2": player_deck[4:8],
            "opponent_deck": opponent_deck,
            "opponent_deck1": opponent_deck[0:4],
            "opponent_deck2": opponent_deck[4:8],
        }
        
        battles_info.append(battle_info)
    
    return battles_info

@app.route('/analyze', methods=['GET'])
def analyze():
    global weaknesses, strengths, summary, ptag
    
    print(get_battle_info(ptag))
    ai_output = (format_ai(ai_analyze(list_to_string(get_battle_info(ptag)))))
    print(ai_output)
    strengths = ai_output[0]
    weaknesses = ai_output[1]
    summary = ai_output[2]
    return jsonify({'strengths': strengths, 'weaknesses': weaknesses, 'summary': summary})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    global ptag
    player_tag = request.form['player_tag']
    ptag = player_tag
    print(f'Submitted player tag: {ptag}')  # Debugging output
    return redirect(url_for('show_battles', player_tag=player_tag))

@app.route('/compare', methods=['GET', 'POST'])
def compare():
    analysis_result = None
    if request.method == 'POST':
        player1 = list_to_string(get_battle_info(request.form['player1']))
        player2 = list_to_string(get_battle_info(request.form['player2']))

        comparison_data =  f"{player1} next player data: \n{player2}"
        print(player2)

        analysis_result = ai_compare(comparison_data)
    return render_template('compare.html', analysis_result=analysis_result)

@app.route('/leaderboards', methods=['GET'])
def leaderboards():
    return render_template('leaderboards.html')

@app.route('/<player_tag>', methods=['GET'])
def show_battles(player_tag):
    print(ptag)
    battles_info = get_battle_info(player_tag)
    return render_template('battles.html', battles=battles_info, weaknesses=weaknesses)

if __name__ == '__main__':
    app.run(debug=True, port=3000)