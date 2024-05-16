import openai
from battle_fetch import recBattles

# Set your OpenAI API key
openai.api_key = 'sk-proj-idVk1xalB2iTO46UcOYvT3BlbkFJL4KwhQMd99sX0rXS3xey'

def analyze_battles(battles):
    cards_won_against = []
    cards_lost_against = []

    for battle in battles:
        team_win_status = battle["team"]["win_status"]
        opponent_deck = battle["opponent"]["deck"]

        if team_win_status == "win":
            cards_won_against.extend(card["name"] for card in opponent_deck)
        else:
            cards_lost_against.extend(card["name"] for card in opponent_deck)
    
    cards_won_against_freq = {card: cards_won_against.count(card) for card in set(cards_won_against)}
    cards_lost_against_freq = {card: cards_lost_against.count(card) for card in set(cards_lost_against)}

    prompt = f"Analyze the following data:\n\nCards the player frequently won against:\n{cards_won_against_freq}\n\nCards the player frequently lost against:\n{cards_lost_against_freq}\n\nProvide a summary of which cards the player is strong or weak against and suggest improvements."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return "This is the analysis result."
    return response['choices'][0]['message']['content'].strip()

# Fetch recent battles

