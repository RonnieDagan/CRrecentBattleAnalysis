import requests
import json
import requests

class recBattles:
    

    def __init__(self, API_TOKEN, PLAYER_TAG):
        self.API_TOKEN = API_TOKEN
        self.PLAYER_TAG= PLAYER_TAG

    def check_win(self, player_crowns, opponent_crowns):
        if player_crowns > opponent_crowns:
            return 'win'
        elif opponent_crowns > player_crowns:
            return 'loss'
        else:
            return 'draw'

    def check_opponent_win(self, win):
        if win == "win":
            return 'loss'
        elif win == 'draw':
            return 'draw'
        return 'win'

    def recent_battles(self):
        
        output = []

        # Construct the API URL
        url = f'https://api.clashroyale.com/v1/players/%23{self.PLAYER_TAG}/battlelog'

        # Make the API request
        headers = {'Authorization': f'Bearer {self.API_TOKEN}'}
        response = requests.get(url, headers=headers)
        battle_log = response.json()

        for battle in battle_log:
            team = battle.get("team")
            opponent = battle.get("opponent")

            team_win = self.check_win(team[0]["crowns"], opponent[0]["crowns"])
            opponent_win = self.check_opponent_win(team_win)
            team_name = team[0]["name"]
            opponent_name = opponent[0]["name"]

            add_output = {
                "game_info": {
                    "mode": battle["gameMode"]["name"],
                    "type": battle["type"],
                },
                "team": {
                    "name": team_name,
                    "tag": team[0]["tag"],
                    "startingTrophies": team[0]["startingTrophies"], 
                    "win_status": team_win,
                    "crowns": team[0]["crowns"],
                    "deck": [],
                },
                "opponent": {
                    "name": opponent_name,
                    "tag": opponent[0]["tag"],
                    "startingTrophies": opponent[0]["startingTrophies"], 
                    "win_status": opponent_win,
                    "crowns": opponent[0]["crowns"],
                    "deck": [],
                }
            }

            for card in team[0]['cards']:
                current_card = {
                    "name": card["name"],
                    "level": (14 - card["maxLevel"]) + card["level"],
                    # "elixirCost": card["elixirCost"],
                    "iconUrl": card["iconUrls"]["medium"],
                }
                add_output["team"]["deck"].append(current_card)

            for card in opponent[0]['cards']:
                current_card = {
                    "name": card["name"],
                    "level": (14 - card["maxLevel"]) + card["level"],
                    # "elixirCost": card["elixirCost"],
                    "iconUrl": card["iconUrls"]["medium"],
                }
                add_output["opponent"]["deck"].append(current_card)

            output.append(add_output)

            
        return output