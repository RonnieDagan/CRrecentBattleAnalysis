
"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""



import os

import google.generativeai as genai

genai.configure(api_key="")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
  system_instruction="I will pass in lists of player data for the game clash royale. List cards the player does well against and cards he does bad against in this format. \n\nCards that {player name} played well against:\nCard 1\ncard 2\ncard \netc\nCards that {player name} played poorly against\ncard 1\netc\n\nits important that u only list the cards not describe them in any way. Thats it also only list about 5-10 cards for each strength or weakness do not overwhelm with info. Also only analyze the player not the opponent.\nyou can also give a short sumamry at the end, for information about the cards use https://clashroyale.fandom.com/wiki/Card_Overviews, also format like how i did, dont add  * to signify bullets.\n"
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "{\n        \"game_info\": {\n            \"mode\": \"EventDeck_SpellCauldron\",\n            \"type\": \"seasonalBattle\"\n        },\n        \"team\": {\n            \"name\": \"l Ronnie l\",\n            \"tag\": \"#J2LJQY0U\",\n            \"startingTrophies\": 7411,\n            \"win_status\": \"loss\",\n            \"crowns\": 1,\n            \"deck\": [\n                {\n                    \"name\": \"Clone\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/mHVCet-1TkwWq-pxVIU2ZWY9_2z7Z7wtP25ArEUsP_g.png\"\n                },\n                {\n                    \"name\": \"Rage\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/bGP21OOmcpHMJ5ZA79bHVV2D-NzPtDkvBskCNJb7pg0.png\"\n                },\n                {\n                    \"name\": \"Freeze\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/I1M20_Zs_p_BS1NaNIVQjuMJkYI_1-ePtwYZahn0JXQ.png\"\n                },\n                {\n                    \"name\": \"Mirror\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/wC6Cm9rKLEOk72zTsukVwxewKIoO4ZcMJun54zCPWvA.png\"\n                },\n                {\n                    \"name\": \"Goblin Barrel\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/CoZdp5PpsTH858l212lAMeJxVJ0zxv9V-f5xC8Bvj5g.png\"\n                },\n                {\n                    \"name\": \"Skeleton Army\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/fAOToOi1pRy7svN2xQS6mDkhQw2pj9m_17FauaNqyl4.png\"\n                },\n                {\n                    \"name\": \"Goblin Gang\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/NHflxzVAQT4oAz7eDfdueqpictb5vrWezn1nuqFhE4w.png\"\n                },\n                {\n                    \"name\": \"Princess\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/bAwMcqp9EKVIKH3ZLm_m0MqZFSG72zG-vKxpx8aKoVs.png\"\n                }\n            ]\n        },\n        \"opponent\": {\n            \"name\": \"Yusuf050\",\n            \"tag\": \"#2RY9GY8V\",\n            \"startingTrophies\": 7283,\n            \"win_status\": \"win\",\n            \"crowns\": 2,\n            \"deck\": [\n                {\n                    \"name\": \"Lumberjack\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/E6RWrnCuk13xMX5OE1EQtLEKTZQV6B78d00y8PlXt6Q.png\"\n                },\n                {\n                    \"name\": \"Balloon\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/qBipxLo-3hhCnPrApp2Nn3b2NgrSrvwzWytvREev0CY.png\"\n                },\n                {\n                    \"name\": \"Prince\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/3JntJV62aY0G1Qh6LIs-ek-0ayeYFY3VItpG7cb9I60.png\"\n                },\n                {\n                    \"name\": \"Valkyrie\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/0lIoYf3Y_plFTzo95zZL93JVxpfb3MMgFDDhgSDGU9A.png\"\n                },\n                {\n                    \"name\": \"Inferno Tower\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/GSHY_wrooMMLET6bG_WJB8redtwx66c4i80ipi4gYOM.png\"\n                },\n                {\n                    \"name\": \"Minions\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/yHGpoEnmUWPGV_hBbhn-Kk-Bs838OjGzWzJJlQpQKQA.png\"\n                },\n                {\n                    \"name\": \"Zap\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/7dxh2-yCBy1x44GrBaL29vjqnEEeJXHEAlsi5g6D1eY.png\"\n                },\n                {\n                    \"name\": \"Arrows\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/Flsoci-Y6y8ZFVi5uRFTmgkPnCmMyMVrU7YmmuPvSBo.png\"\n                }\n            ]\n        }\n    },\n    {\n        \"game_info\": {\n            \"mode\": \"TeamVsTeam\",\n            \"type\": \"seasonalBattle\"\n        },\n        \"team\": {\n            \"name\": \"Killerslurpies\",\n            \"tag\": \"#Y0L09YGV2\",\n            \"startingTrophies\": 6261,\n            \"win_status\": \"loss\",\n            \"crowns\": 0,\n            \"deck\": [\n                {\n                    \"name\": \"Rage\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/bGP21OOmcpHMJ5ZA79bHVV2D-NzPtDkvBskCNJb7pg0.png\"\n                },\n                {\n                    \"name\": \"Dart Goblin\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/BmpK3bqEAviflqHCdxxnfm-_l3pRPJw3qxHkwS55nCY.png\"\n                },\n                {\n                    \"name\": \"Mirror\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/wC6Cm9rKLEOk72zTsukVwxewKIoO4ZcMJun54zCPWvA.png\"\n                },\n                {\n                    \"name\": \"Clone\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/mHVCet-1TkwWq-pxVIU2ZWY9_2z7Z7wtP25ArEUsP_g.png\"\n                },\n                {\n                    \"name\": \"Freeze\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/I1M20_Zs_p_BS1NaNIVQjuMJkYI_1-ePtwYZahn0JXQ.png\"\n                },\n                {\n                    \"name\": \"Goblin Barrel\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/CoZdp5PpsTH858l212lAMeJxVJ0zxv9V-f5xC8Bvj5g.png\"\n                },\n                {\n                    \"name\": \"Ice Golem\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/r05cmpwV1o7i7FHodtZwW3fmjbXCW34IJCsDEV5cZC4.png\"\n                },\n                {\n                    \"name\": \"Goblin Gang\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/NHflxzVAQT4oAz7eDfdueqpictb5vrWezn1nuqFhE4w.png\"\n                }\n            ]\n        },\n        \"opponent\": {\n            \"name\": \"romero07\",\n            \"tag\": \"#CYU88L989\",\n            \"startingTrophies\": 6081,\n            \"win_status\": \"win\",\n            \"crowns\": 3,\n            \"deck\": [\n                {\n                    \"name\": \"Mini P.E.K.K.A\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/Fmltc4j3Ve9vO_xhHHPEO3PRP3SmU2oKp2zkZQHRZT4.png\"\n                },\n                {\n                    \"name\": \"Inferno Dragon\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/y5HDbKtTbWG6En6TGWU0xoVIGs1-iQpIP4HC-VM7u8A.png\"\n                },\n                {\n                    \"name\": \"Princess\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/bAwMcqp9EKVIKH3ZLm_m0MqZFSG72zG-vKxpx8aKoVs.png\"\n                },\n                {\n                    \"name\": \"Wizard\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/Mej7vnv4H_3p_8qPs_N6_GKahy6HDr7pU7i9eTHS84U.png\"\n                },\n                {\n                    \"name\": \"P.E.K.K.A\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/MlArURKhn_zWAZY-Xj1qIRKLVKquarG25BXDjUQajNs.png\"\n                },\n                {\n                    \"name\": \"Skeleton Army\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/fAOToOi1pRy7svN2xQS6mDkhQw2pj9m_17FauaNqyl4.png\"\n                },\n                {\n                    \"name\": \"Zap\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/7dxh2-yCBy1x44GrBaL29vjqnEEeJXHEAlsi5g6D1eY.png\"\n                },\n                {\n                    \"name\": \"Fireball\",\n                    \"level\": 11,\n                    \"iconUrl\": \"https://api-assets.clashroyale.com/cards/300/lZD9MILQv7O-P3XBr_xOLS5idwuz3_7Ws9G60U36yhc.png\"\n                }\n            ]\n        }\n    },",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Cards that l Ronnie l played well against:\nInferno Tower\nMinions\nZap\nArrows\n\nCards that l Ronnie l played poorly against:\nLumberjack\nBalloon\nPrince\nValkyrie\n\nSummary:  l Ronnie l struggled against heavy beatdown decks. This is likely due to not having enough answers for strong pushes, such as a Valkyrie or P.E.K.K.A. They played well against decks with weaker pushes or more control elements, as they have many answers for those strategies. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "tell me about inferno tower\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "The Inferno Tower is a defensive building that prioritizes high-hitpoint targets. It has a high damage output and can quickly eliminate tanky units like the Giant, Golem, or P.E.K.K.A., making it a strong counter against those threats. \n\nHere are some key features of the Inferno Tower:\n\n* **High Damage:** It deals significant damage per second to its target.\n* **Target Priority:** It prioritizes high-hitpoint units, ignoring lower-health targets until they are eliminated.\n* **Slow Firing Rate:** It has a relatively slow firing speed.\n* **Slow-Moving:** It is immobile and cannot move.\n* **Defensive Building:** It is best utilized as a defensive structure, but can also be used to counter pushes.\n\n**Strengths:**\n\n* Excellent against high-hitpoint units.\n* Can eliminate tanky units quickly.\n* Strong defensive building.\n\n**Weaknesses:**\n\n* Can be easily distracted by low-health units.\n* Slow firing rate can make it ineffective against fast-moving units.\n* Susceptible to splash damage spells like Fireball or Rocket.\n* Cannot attack air units.\n\n**Overall:**\n\nThe Inferno Tower is a powerful defensive building that can be a crucial asset in a deck. Its high damage output and target priority make it a strong counter against many popular offensive strategies. However, its slow firing rate and susceptibility to splash damage spells can be weaknesses. \n",
      ],
    },
  ]
)
def ai_analyze(message):
  response = chat_session.send_message(message)
  
  # file_name = 'output.txt'

  # # Open the file in write mode
  # with open(file_name, 'w') as file:
  #     # Write the long string to the file
  #     file.write(response.text)
  return response.text